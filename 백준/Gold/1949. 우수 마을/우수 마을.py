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


def solution(node):
    visited[node] = True
    memo[node][1] += weights[node]
    for x in tree[node]:
        if not visited[x]:
            solution(x)
            memo[node][1] += memo[x][0]
            memo[node][0] += max(memo[x])

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    # n, m = map(int, input().split())
    # lst = [*map(int, input().split())]
    n = int(input())
    weights = [0] + [*map(int, input().split())]
    tree = defaultdict(list)
    for _ in range(n-1):
        a, b = S()
        tree[a].append(b)
        tree[b].append(a)
    memo = [[0, 0] for _ in range(n+1)]
    visited = [False] * (n+1)
    
    # output
    solution(1)
    print(max(memo[1]))