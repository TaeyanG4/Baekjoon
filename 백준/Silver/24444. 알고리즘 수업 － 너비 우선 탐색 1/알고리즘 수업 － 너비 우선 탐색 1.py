## taeyang's template (1.0.1)
#################################
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import time
# import pprint
from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
#################################

def bfs(start):
    global ans, cnt

    q = deque()
    q.append(start)
    ans[start] = cnt
    
    while q:
        v = q.popleft()
        for nv in sorted(graph[v]):
            if not ans[nv]:
                cnt += 1
                ans[nv] = cnt
                q.append(nv)

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m, r = map(int, input().split())
    ans, cnt = [0] * (n+1), 1
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n + 1)
    
    # output
    bfs(r)
    ans.pop(0)
    for v in ans:
        print(v)