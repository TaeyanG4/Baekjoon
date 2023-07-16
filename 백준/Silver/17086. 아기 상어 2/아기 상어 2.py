# import lines
#################################
import sys
# import math
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

def solution():
    
    dq = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                dq.append((i, j))

    while dq:
        y, x = dq.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not board[ny][nx]:
                dq.append((ny, nx))
                board[ny][nx] = board[y][x] + 1
    return max(map(max, board)) - 1

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