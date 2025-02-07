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
#################################


def solution():
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    d, n = [*map(str, input().split())]
    n = int(n)
    board = [list(S()) for _ in range(n)]
    
    if d == 'L' or d == 'R':
        board = [list(reversed(i)) for i in board]     
    else:
        board = board[::-1]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 5
            elif board[i][j] == 5:
                board[i][j] = 2
            elif board[i][j] == 1 or board[i][j] == 8:
                continue
            else:
                board[i][j] = '?'
                    
    for line in board:
        print(*line)