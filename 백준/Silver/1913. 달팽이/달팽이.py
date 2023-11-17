## taeyang's template (1.0.8)
#################################
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
# from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
# from functools import *
#################################


def solution():
    pass    
    

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # input
    n = int(input())
    m = int(input())
    board = [[0] * n for _ in range(n)]
    py, px = 0, 0
    y, x = 0, 0
    cnt = n * n
    d = 0
    
    # implement
    while True:
        board[y][x] = cnt
        dy, dx = direction[d]
        ny, nx = y + dy, x + dx
        
        # 위치 저장
        if m == cnt:
                py, px = y + 1, x + 1
        
        # 다음 위치가 범위 내이고, 0이면 이동
        if 0 <= ny < n and 0 <= nx < n and not board[ny][nx]:
            cnt -= 1
            y, x = ny, nx
        # 범위를 벗어나거나, 이미 값이 있으면 방향 전환
        else:
            if cnt == 1:
                break
            d = (d + 1) % 4
    
    # output
    for line in board:
        print(*line)
    print(py, px)