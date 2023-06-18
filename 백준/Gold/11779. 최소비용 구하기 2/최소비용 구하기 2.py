# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################
    
def solution(n, m, mat, start, end):
    pq = [(0, start)]
    while pq:
        d, n = heappop(pq)
        if d > dist[n]:
            continue
        
        for nxt, nxtDist in graph[n]:
            cost = d + nxtDist
            if cost < dist[nxt]:
                dist[nxt] = cost
                near[nxt] = n
                heappush(pq, (cost, nxt))

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n = int(input())
    m = int(input())
    graph = defaultdict(list)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    start, end = map(int, input().split())
    
    dist = [sys.maxsize] * (n+1)
    near = [start] * (n+1)
    
    # output
    solution(n, m, graph, start, end)
    
    ans = []
    p = end
    while start != p:
        ans.append(str(p))
        p = near[p]
    
    ans.append(str(start))
    ans.reverse()
    
    print(dist[end])
    print(len(ans))
    print(' '.join(ans))

