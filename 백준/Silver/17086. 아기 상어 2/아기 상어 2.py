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

def bfs(y, x, cnt):
    
    cnt = 0
    q = deque([(y, x, cnt)])
    visited = [[False] * m for _ in range(n)]
    visited[y][x] = True

    while q:
        y, x, cnt = q.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if board[ny][nx]:
                    return cnt + 1
                else:
                    visited[ny][nx] = True
                    q.append((ny, nx, cnt + 1))

def solution():
    
    max_val = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                max_val = max(max_val, bfs(i, j, 0))

    return max_val

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # input
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    # output
    print(solution())