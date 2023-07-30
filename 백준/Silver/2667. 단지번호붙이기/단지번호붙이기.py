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

def bfs(board, n, y, x):
    q = deque([(y, x)])
    board[y][x] = 0
    cnt = 1
    while q:
        y, x = q.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 1:
                board[ny][nx] = 0
                q.append((ny, nx))
                cnt += 1
    return cnt

def solution(n, board):
    ans = []
    for y in range(n):
        for x in range(n):
            if board[y][x] == 1:
                ans.append(bfs(board, n, y, x))
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    board = [list(map(int, input().strip())) for _ in range(n)]
    
    # output
    ans = solution(n, board)
    print(len(ans))
    for a in sorted(ans):
        print(a)