# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import time
# import pprint
from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def bfs(shark):
    
    global exp, level, move_cnt
    
    q = deque([shark])
    distance = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    visited[shark[0]][shark[1]] = True
    nearest_fishs = [] # 근처 물고기들의 거리, y, x
    
    while q:
        y, x = q.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and mat[ny][nx] <= level:
                distance[ny][nx] = distance[y][x] + 1
                if 0 < mat[ny][nx] < level:
                    nearest_fishs.append((distance[ny][nx], ny, nx))
                else:
                    visited[ny][nx] = True
                    q.append((ny, nx))
    
    if not nearest_fishs:
        return -1, -1, -1
    else:
        nearest_fishs.sort()
        return nearest_fishs[0]

def solution():
    
    global move_cnt, exp, level, shark_p
    
    while True:
        
        # find nearest fish
        dist, y, x = bfs(shark_p)
        if dist == -1:
            break
        
        # upadte info
        shark_p = (y, x)
        mat[y][x] = 0
        move_cnt += dist
        exp += 1
        if exp == level:
            level += 1
            exp = 0
    
if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    move_cnt, exp, level = 0, 0, 2 # move_cnt: 이동거리, exp: 경험치, level: 현재 레벨
    for r in range(n):
        for c in range(n):
            if mat[r][c] == 9:
                shark_p = (r, c)
                mat[r][c] = 0
                break
    
    # output
    solution()
    print(move_cnt)