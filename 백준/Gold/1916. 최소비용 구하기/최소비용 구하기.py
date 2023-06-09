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
    heappush(pq, [start, 0])
    visited[start] = 0
    
    while pq:
        s, d = heappop(pq)
        if visited[s] < d:
            continue
        for nx, nw in graph[s]:
            nd = d + nw
            if nd < visited[nx]:
                visited[nx] = nd
                heappush(pq, [nx, nd])

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = int(input())
    m = int(input())
    graph = defaultdict(list)
    visited = [sys.maxsize] * (n+1)
    all_pay = list()
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
    start, end = map(int, input().split())
    
    # output
    solution(start)
    print(visited[end])