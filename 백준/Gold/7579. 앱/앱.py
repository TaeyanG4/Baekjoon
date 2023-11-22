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
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # input
    n, m = map(int, input().split())
    app = [*map(int, input().split())]
    cost = [*map(int, input().split())]
    
    # knapsack
    ans = INF
    memo = [[0 for _ in range(sum(cost)+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(sum(cost)+1):
            if cost[i] > j:
                memo[i][j] = memo[i-1][j]
            else:
                memo[i][j] = max(memo[i-1][j], memo[i-1][j-cost[i]] + app[i])
                
            if memo[i][j] >= m:
                ans = min(ans, j)
    
    # output
    if m == 0:
        print(0)
    elif n == 1:
        print(cost[0])
    elif ans == INF:
        print(n * m)
    else:
        print(ans)