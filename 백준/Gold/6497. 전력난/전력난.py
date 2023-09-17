## taeyang's template (1.0.6)
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

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

def solution(cost):
    
    # Kruskal's algorithm
    elist.sort(key=lambda x: x[2])
    for s, e, w in elist:
        sroot, eroot = find(s), find(e)
        if sroot != eroot:
            union(s, e)
            cost -= w
    
    return cost

if __name__ == '__main__':
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    # n, m = map(int, input().split())
    # lst = [*map(int, input().split())]
    # n = int(input())
    
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break
        parents = [i for i in range(m)]
        elist = []
        cost = 0
        for _ in range(n):
            x, y, z = map(int, input().split())
            elist.append([x, y, z])
            cost += z
        
        # output
        print(solution(cost))