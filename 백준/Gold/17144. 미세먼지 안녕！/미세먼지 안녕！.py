# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################

def spread(r, c, mat):
    spread_mat = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            cnt = 0
            if mat[i][j] > 0:
                for dy, dx in direction:
                    ny, nx = dy + i, dx + j
                    if 0 <= ny < r and 0 <= nx < c and mat[ny][nx] != -1:
                        cnt += 1
                        spread_mat[ny][nx] += mat[i][j] // 5
                spread_mat[i][j] += mat[i][j] - (mat[i][j] // 5) * cnt
                
    for i in range(r):
        for j in range(c):
            mat[i][j] = spread_mat[i][j]

def run_cleaner(r, c, mat):
    up_cleaner = cleaner[0][0]
    down_cleaner = cleaner[1][0]
    moved_mat = copy.deepcopy(mat)
    
    moved_mat[0][:-1] = mat[0][1:]
    moved_mat[-1][:-1] = mat[-1][1:]
    
    moved_mat[up_cleaner][2:] = mat[up_cleaner][1:-1]
    moved_mat[down_cleaner][2:] = mat[down_cleaner][1:-1]
    
    for i in range(1, up_cleaner+1):
        moved_mat[i-1][-1] = mat[i][-1]
    
    for i in range(down_cleaner+2, r):
        moved_mat[i-1][0] = mat[i][0]
    
    for i in range(0, up_cleaner-1):
        moved_mat[i+1][0] = mat[i][0]
    
    for i in range(down_cleaner, r-1):
        moved_mat[i+1][-1] = mat[i][-1]
        
    moved_mat[up_cleaner][1] = 0
    moved_mat[down_cleaner][1] = 0
    moved_mat[up_cleaner][0] = -1
    moved_mat[down_cleaner][0] = -1

    for i in range(r):
        for j in range(c):
            mat[i][j] = moved_mat[i][j]
    
def print_sum_mat():
    sum_val = 0
    for i in range(r):
        for j in range(c):
            if mat[i][j] > 0:
                sum_val += mat[i][j]
    return sum_val
    
def solution(r, c, t, mat):
    for i in range(t):
        # 확산
        # print(f'time {i}')
        spread(r, c, mat)
        # pprint.pprint(mat)
        
        # 정화
        run_cleaner(r, c, mat)
        # pprint.pprint(mat)
        

    # 합산
    return print_sum_mat()

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    r, c, t = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(r)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cleaner = []
    temp = 0
    for i in mat:
        if i[0] == -1:
            cleaner.append((temp, 0))
        temp += 1
    
    # output
    print(solution(r, c, t, mat))
