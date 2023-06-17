# https://kyun2da.github.io/2021/04/20/brownsmog/

import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

up = -1
down = -1
# 공기 청정기 위치 찾기
for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break

# 미세먼지 확산
def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        tmp_arr[nx][ny] += arr[i][j] // 5
                        tmp += arr[i][j] // 5
                arr[i][j] -= tmp

    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp_arr[i][j]

# 공기청정기 위쪽 이동
def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny


for _ in range(t):
    spread()
    air_up()
    air_down()

answer = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            answer += arr[i][j]

print(answer)

# import lines
# #################################
# import sys
# import math
# import copy
# # import ast
# # import re
# # import time
# # import json
# import pprint
# from collections import *
# from heapq import *
# from itertools import *
# # from datetime import datetime
# #################################

# def spread(r, c, mat):
#     spread_mat = [[0] * c for _ in range(r)]
#     for i in range(r):
#         for j in range(c):
#             cnt = 0
#             if mat[i][j] > 0:
#                 for dy, dx in direction:
#                     ny, nx = dy + i, dx + j
#                     if 0 <= ny < r and 0 <= nx < c and mat[ny][nx] != -1:
#                         cnt += 1
#                         spread_mat[ny][nx] += mat[i][j] // 5
#                 spread_mat[i][j] += mat[i][j] - (mat[i][j] // 5) * cnt
                
#     for i in range(r):
#         for j in range(c):
#             mat[i][j] = spread_mat[i][j]

# def run_cleaner(r, c, mat):
#     up_cleaner = cleaner[0][0]
#     down_cleaner = cleaner[1][0]
#     moved_mat = copy.deepcopy(mat)
    
#     moved_mat[0][:-1] = mat[0][1:]
#     moved_mat[-1][:-1] = mat[-1][1:]
    
#     moved_mat[up_cleaner][2:] = mat[up_cleaner][1:-1]
#     moved_mat[down_cleaner][2:] = mat[down_cleaner][1:-1]
    
#     for i in range(1, up_cleaner+1):
#         moved_mat[i-1][-1] = mat[i][-1]
    
#     for i in range(down_cleaner+2, r):
#         moved_mat[i-1][0] = mat[i][0]
    
#     for i in range(0, up_cleaner-1):
#         moved_mat[i+1][0] = mat[i][0]
    
#     for i in range(down_cleaner, r-1):
#         moved_mat[i+1][-1] = mat[i][-1]
        
#     moved_mat[up_cleaner][1] = 0
#     moved_mat[down_cleaner][1] = 0
#     moved_mat[up_cleaner][0] = -1
#     moved_mat[down_cleaner][0] = -1

#     for i in range(r):
#         for j in range(c):
#             mat[i][j] = moved_mat[i][j]
    
# def print_sum_mat():
#     sum_val = 0
#     for i in range(r):
#         for j in range(c):
#             if mat[i][j] > 0:
#                 sum_val += mat[i][j]
#     return sum_val
    
# def solution(r, c, t, mat):
#     for i in range(t):
#         # 확산
#         # print(f'time {i}')
#         spread(r, c, mat)
#         # pprint.pprint(mat)
        
#         # 정화
#         run_cleaner(r, c, mat)
#         # pprint.pprint(mat)
        

#     # 합산
#     return print_sum_mat()

# if __name__ == '__main__':
#     input = sys.stdin.readline
#     # sys.setrecursionlimit(10**9)
    
#     # input
#     r, c, t = map(int, input().split())
#     mat = [list(map(int, input().split())) for _ in range(r)]
#     direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     cleaner = []
#     temp = 0
#     for i in mat:
#         if i[0] == -1:
#             cleaner.append((temp, 0))
#         temp += 1
    
#     # output
#     print(solution(r, c, t, mat))

