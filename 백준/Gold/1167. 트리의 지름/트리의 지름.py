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
    q = deque()
    dist = [-1] * (v+1)
    q.append((start, 0))
    dist[start] = 0
    while q:
        node, cost = q.popleft()
        for nxt, cost in graph[node]:
            if dist[nxt] == -1:
                dist[nxt] = dist[node] + cost
                q.append((nxt, cost))
    
    max_val = max(dist)
    index = dist.index(max_val)
    return index, max_val

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    v = int(input())
    graph = defaultdict(list)
    for i in range(v):
        li = list(map(int, input().split()))
        node = li[0]
        j = 1
        while True:
            a = li[j]
            if a == -1:
                break
            else:
                b = li[j+1]
                graph[node].append((a, b))
                j += 2
            
    # output
    s, max_dist = solution(1)
    e, max_dist = solution(s)
    print(max_dist)
    