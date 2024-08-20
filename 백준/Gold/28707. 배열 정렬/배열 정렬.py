## taeyang's template (1.0.8)
# https://velog.io/@vkdldjvkdnj/boj28707
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
from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
# from functools import *
#################################


def solution(n, tup, m, lrc):
    
    pq = [(0, tup)]
    dist = defaultdict(int)
    dist[tup] = 0
    while pq:
        cost, state = heappop(pq)
        if dist[state] < cost:
            continue
        for l, r, c in lrc:
            nxt = list(state)
            nxt[l-1], nxt[r-1] = nxt[r-1], nxt[l-1]
            nxt = tuple(nxt)
            if nxt not in dist or dist[nxt] > cost + c:
                dist[nxt] = cost + c
                heappush(pq, (cost + c, nxt))
                
    return -1 if tuple(sorted(tup)) not in dist.keys() else dist[tuple(sorted(tup))]

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # input
    n = int(input())
    tup = tuple(S())
    m = int(input())
    lrc = [tuple(S()) for _ in range(m)]
         
    
    # output
    print(solution(n, tup, m, lrc))