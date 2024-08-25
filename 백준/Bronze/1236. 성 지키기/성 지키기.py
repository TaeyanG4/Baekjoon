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
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # input
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    
    # output
    vert, hori = [False] * n, [False] * m
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'X':
                vert[i] = True
                hori[j] = True
    ans = max(vert.count(False), hori.count(False))
    print(ans)