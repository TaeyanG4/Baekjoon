# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

# https://ca.ramel.be/166

def solution(x, low, ids, visited, stack):
    global id_val
    ids[x], low[x] = id_val, id_val
    id_val += 1
    visited[x] = True
    stack.append(x)
    
    for i in graph[x]:
        if ids[i] == -1:
            solution(i, low, ids, visited, stack)
            low[x] = min(low[x], low[i])
        elif visited[i]:
            low[x] = min(low[x], ids[i])
    
    w = -1
    scc = []
    if low[x] == ids[x]:
        while w != x:
            w = stack.pop()
            scc.append(w)
            visited[w] = False
        res.append(sorted(scc))

if __name__ == '__main__':
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    
    # input
    v, e = map(int, input().split())
    graph = defaultdict(list)
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    stack = []
    low = [-1] * (v+1)
    ids = [-1] * (v+1)
    visited = [False] * (v+1)
    id_val = 0
    res = []
    
    for i in range(1, v+1):
        if ids[i] == -1:
            
            # dfs
            solution(i, low, ids, visited, stack)
    
    # output
    print(len(res))
    for li in sorted(res):
        print(*li, -1)