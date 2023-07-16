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

def bfs(y, x):
    q = deque([(y, x)])
    visited[y][x] = True
    cnt = 1
    
    while q:
        y, x = q.popleft()
        zeros[y][x] = group_cnt
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and not board[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True
                cnt += 1
                
    return cnt

def cntMove(y, x):
    candidates = set()
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and zeros[ny][nx]:
            candidates.add(zeros[ny][nx])

    cnt = 1
    for c in candidates:
        cnt += info[c]

    return cnt % 10

def solution():
    global group_cnt
    res_board = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 and not visited[i][j]:
                visited[i][j] = True
                info[group_cnt] = bfs(i, j)
                group_cnt += 1
                
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                res_board[i][j] = cntMove(i, j)
                
    return res_board

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    zeros = [[0] * m for _ in range(n)]
    group_cnt = 1
    info = defaultdict(int)
    
    # output
    for line in solution():
        print(*line, sep='')