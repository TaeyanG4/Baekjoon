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
from itertools import *
# from datetime import datetime
#################################

def solution(start):
    pq = []
    dist = [sys.maxsize] * (n + 1)
    heappush(pq, (0, start))
    dist[start] = 0
    while pq:
        d, now = heappop(pq)
        if dist[now] < d:
            continue
        for i in edge[now]:
            cost = d + i[0]
            
            if cost < dist[i[1]]:
                dist[i[1]] = cost
                heappush(pq, (cost, i[1]))
                
    return dist

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n, e = map(int, input().split())
    edge = defaultdict(list)
    
    for _ in range(e):
        u, v, w = map(int, input().split())
        edge[u].append((w, v))
        edge[v].append((w, u))
        
    v1, v2 = map(int, input().split())
    
    # output
    ori_dist = solution(1)
    v1_dist = solution(v1)
    v2_dist = solution(v2)
    
    
    # 1 => v1 => v2 => N
    v1_path = ori_dist[v1] + v1_dist[v2] + v2_dist[n]
    # 1 => v2 => v1 => N
    v2_path = ori_dist[v2] + v2_dist[v1] + v1_dist[n]
    
    ans = min(v1_path, v2_path)
    
    print(ans if ans < sys.maxsize else -1)
