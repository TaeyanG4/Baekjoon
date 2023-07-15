# import lines
#################################
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
from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(n, m, ind, graph):
    res, pq = [], []
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        ind[b] += 1
        
    for i in range(1, n + 1):
        if ind[i] == 0:
            heappush(pq, i)
    
    while pq:
        tmp = heappop(pq)
        res.append(tmp)
        for i in graph[tmp]:
            ind[i] -= 1
            if ind[i] == 0:
                heappush(pq, i)
    return res

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    # INF = sys.maxsize
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    ind = [0] * (n + 1)
    graph = defaultdict(list)
    
    # output
    print(*solution(n, m, ind, graph))