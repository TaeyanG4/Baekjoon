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
from collections import *
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


def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    for i in range(15, -1, -1):
        if depth[a] - depth[b] >= (1 << i):
            a = parent[a][i]
    if a == b:
        return a
    for i in range(15, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]


def dfs(node, dep, d):
    depth[node] = dep
    dist[node] = d
    for nxt, w in graph[node]:
        if depth[nxt] == -1:
            parent[nxt][0] = node
            dfs(nxt, dep+1, d+w)


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    n = int(input())
    graph = defaultdict(list)
    depth = [-1] * (n+1)
    dist = [0] * (n+1)
    parent = [[0] * 16 for _ in range(n+1)] 
    for _ in range(n-1):
        a, b, d = S()
        graph[a].append((b, d))
        graph[b].append((a, d))

    # 사전작업 (dfs, parent)
    dfs(1, 0, 0)
    for j in range(1, 16):
        for i in range(1, n+1):
            parent[i][j] = parent[parent[i][j-1]][j-1]

    m = int(input())
    for _ in range(m):
        a, b = S()
        anc = lca(a, b)
        ans = dist[a] + dist[b] - 2*dist[anc]
        print(ans)