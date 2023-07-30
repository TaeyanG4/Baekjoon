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

def solution(n, m, board):
    
    # bfs
    q = deque([(0, 0)]) # startX, startY (0, 0)부터 시작
    while q:
        y, x = q.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 1:
                board[ny][nx] = board[y][x] + 1
                q.append((ny, nx))
    
    return board[n-1][m-1]

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(n)]
    
    # output
    print(solution(n, m, board))