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
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    n = int(input())
    memo = [[0 for _ in range(2)] for _ in range(n)]
    
    # dp
    memo[0] = [0, 1] # 0: 0, 1: 1
    
    for i in range(1, n):
        memo[i][0] = memo[i-1][0] + memo[i-1][1]
        memo[i][1] = memo[i-1][0]

    # output
    print(sum(memo[n-1]))
