## taeyang's template (1.0.4)
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
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution():
    temp = parent[way[0]]
    for i in way:
        if temp != parent[i]:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    # n, m = map(int, input().split())
    # li = [*map(int, input().split())]
    n, m = int(input()), int(input())
    parent = [i for i in range(n + 1)]
    graph = [[*map(int, input().split())] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                union(i+1, j+1)
    way = list(map(int, input().split()))
    
    # output
    print(solution())