## taeyang's template (1.0.6)
#################################
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
import pprint
from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################

def bfs_find_land(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    board[y][x] = land_cnt
    
    while q:
        y, x = q.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and board[ny][nx]:
                visited[ny][nx] = True
                land_p[land_cnt].append((ny, nx))
                board[ny][nx] = land_cnt
                q.append((ny, nx))
                
def get_dist(y, x, land_num):
    for dy, dx in direction:
        dist = 0
        vy, vx = y, x
        while True:
            ny, nx = vy + dy, vx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == 0:
                    dist += 1
                    vy, vx = ny, nx
                else:
                    if dist > 1:
                        land_dist[land_num][board[ny][nx]] = min(land_dist[land_num][board[ny][nx]], dist)
                    break
            else:
                break

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

def solution():
    
    # kruskal's algorithm
    ans = 0
    elist.sort(key=lambda x: x[2])
    for s, e, w in elist:
        if find(s) != find(e):
            union(s, e)
            ans += w
    
    # check
    for i in range(1, land_cnt):
        if find(i) != find(i+1):
            return -1
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    # find land
    land_cnt = 0
    land_p = defaultdict(list)
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j]:
                land_cnt += 1
                land_p[land_cnt].append((i, j))
                bfs_find_land(i, j)
                
    # get dist
    land_dist = [[INF] * (land_cnt+1) for _ in range(land_cnt+1)]
    for i in range(1, land_cnt+1):
        for y, x in land_p[i]:
            get_dist(y, x, i)
            
    elist = []
    for i in range(1, land_cnt+1):
        for j in range(i+1, land_cnt+1):
            if land_dist[i][j] != INF:
                elist.append((i, j, land_dist[i][j]))
    
    # output
    parents = [i for i in range(land_cnt+1)]
    print(solution())
    