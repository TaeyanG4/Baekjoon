## taeyang's template (1.0.4)
# https://hbj0209.tistory.com/107
# https://seongonion.tistory.com/132
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
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################

def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1-x2)**2 + (y1-y2)**2) ** 0.5

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def solution():
    
    ans = 0
    p, elist = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        p.append((x, y))
        
    for _ in range(m):
        a, b = map(int, input().split())
        union(a-1, b-1)
        
    for i in range(n-1):
        for j in range(i+1, n):
            elist.append((i, j, dist(p[i], p[j])))
            
    # kruskal algorithm
    elist.sort(key=lambda x: x[2])
    for s, e, w in elist:
        sroot, eroot = find(s), find(e)
        if sroot != eroot:
            union(sroot, eroot)
            ans += w
            
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    parent = list(range(n+1))
    
    # output
    print(f'{solution():.2f}')