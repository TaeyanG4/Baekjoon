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


def solution():
    global ans
    start, link = 0, 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                start += board[i][j]
            elif not visited[i] and not visited[j]:
                link += board[i][j]
    ans = min(ans, abs(start - link))
    return


def dfs(depth):
    if depth == n:
        solution()
        return
    
    visited[depth] = True
    dfs(depth + 1)
    visited[depth] = False
    dfs(depth + 1)


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    n = int(input())
    board = [[*map(int, input().split())] for _ in range(n)]
    visited = [False] * n
    ans = INF
    
    # dfs
    dfs(0)

    # output
    print(ans)