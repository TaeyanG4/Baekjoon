## taeyang's template (1.0.3)
# https://www.youtube.com/watch?v=Ppimbaxm8d8&t=328s
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
# from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################

def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur, nxt, cost = edges[j]
            if dist[cur] != INF and dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                if i == n - 1:
                    return True
    return False 

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    edges = []
    dist = [INF] * (n + 1)
    for _ in range(m):
        a, b, d = map(int, input().split())
        edges.append((a, b, d))
    
    # output
    ans = bellman_ford(1)
    if ans:
        print(-1)
    else:
        for i in range(2, n + 1):
            if dist[i] == INF:
                print(-1)
            else:
                print(dist[i])