## taeyang's template (1.0.7)
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


def backtracking(depth, val):
    global ans
    
    if depth == k:
        ans = max(ans, val)
        return
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                for dx, dy in direction:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        visited[nx][ny] += 1
                backtracking(depth + 1, val + board[i][j])
                for dx, dy in direction:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        visited[nx][ny] -= 1

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]

    # input
    # n = int(input())
    # lst = [*map(int, input().split())]
    n, m, k = map(int, input().split())
    board = [list(S()) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    ans = -INF
    
    # backtracking
    backtracking(0, 0)
    
    # output
    print(ans)