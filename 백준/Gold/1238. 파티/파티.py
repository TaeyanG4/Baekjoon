# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
from heapq import *
# from itertools import *
# from datetime import datetime
#################################

def solution(start):
    dist = [float('inf') for _ in range(n+1)]
    pq = list()
    heappush(pq, (0, start))
    dist[start] = 0
    while pq:
        cost, node = heappop(pq)
        if dist[node] < cost:
            continue
        for c, nd in graph[node]:
            if dist[nd] > cost + c:
                dist[nd] = cost + c
                heappush(pq, (cost+c, nd))
    
    return dist
    
if __name__ == '__main__':
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)
    
    # input
    max_val = 0
    graph = defaultdict(list)
    n, m, x = map(int, input().split())
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        
    # ouput
    for i in range(1 ,n+1):
        go = solution(i)
        back = solution(x)
        max_val = max(max_val, go[x]+back[i])
    print(max_val)
