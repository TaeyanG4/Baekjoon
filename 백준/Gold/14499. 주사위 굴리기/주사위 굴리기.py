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
# getcontext().prec = 20
#################################


def solution():
    pass

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 동서북남
    
    n, m ,x, y, k = S()
    board = [[*S()] for _ in range(n)]
    command = [*S()]
    dice = [0] * 6  # 위, 앞, 오, 왼, 뒤, 밑
    for c in command:
        if c == 1:  # 동
            if y + 1 >= m:
                continue
            y += 1
            dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
        elif c == 2:  # 서
            if y - 1 < 0:
                continue
            y -= 1
            dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
        elif c == 3:  # 북
            if x - 1 < 0:
                continue
            x -= 1
            dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
        else:  # 남
            if x + 1 >= n:
                continue
            x += 1
            dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
        
        if board[x][y] == 0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0
        print(dice[0])