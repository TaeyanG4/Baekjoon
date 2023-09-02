## taeyang's template (1.0.4)
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
from collections import *
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
    for i in range(2, n+1):
        memo[i] = memo[i-1] + 1
        graph[i] = i-1
        if i%3 == 0 and memo[i] > memo[i//3] + 1:
            memo[i] = memo[i//3] + 1
            graph[i] = i//3
        if i%2 == 0 and memo[i] > memo[i//2] + 1:
            memo[i] = memo[i//2] + 1
            graph[i] = i//2
    return memo

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    memo = [0] * (n+1)
    graph = defaultdict(int)
    
    # output
    solution()
    print(memo[n])
    while n != 0:
        print(n, end=' ')
        n = graph[n]