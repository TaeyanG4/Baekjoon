## taeyang's template (1.0.7)
# https://jainn.tistory.com/74
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


def solution(x):
    cnt[x] = 1
    for i in graph[x]:
        if not cnt[i]:
            solution(i) # 서브트리의 노드 개수를 구하기위한 dfs
            cnt[x] += cnt[i]


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
    # n = int(input())
    
    n, r, q = map(int, input().split())
    graph = defaultdict(list)
    cnt = [0] * (n+1)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    solution(r)
    
    for _ in range(q):
        # output
        print(cnt[int(input())])
