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
# import statistics as st
# from decimal import *
from collections import *
from itertools import *
from heapq import *
# from datetime import datetime
#################################

def solution(start):
    pq = []
    heappush(pq, (0,start))
    visited[start] = 0
    
    while pq:
        d, s = heappop(pq)
        if visited[s] < d:
            continue
        
        for nw, nx in graph[s]:
            nd = d + nw
            
            if visited[nx] > nd:
                heappush(pq, (nd, nx))
                visited[nx] = nd
                
    return graph

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    v, e = map(int, input().split())
    k = int(input())
    graph = defaultdict(list)
    visited = [sys.maxsize] * (v+1)
    for _ in range(e):
        a, b, w = map(int, input().split())
        graph[a].append([w, b])
    
    # output
    solution(k)
    
    for i in visited[1:]:
        if i == sys.maxsize:
            print('INF')
        else:
            print(i)