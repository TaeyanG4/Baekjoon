# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def dfs(x, depth):
    visited[x] = True
    d[x] = depth
    for node in graph[x]:
        if not visited[node]:
            parent[node] = x
            dfs(node, depth+1)

def solution(a, b):
    # lca
    global parent, d, visited, graph
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

if __name__ == '__main__':
    input = sys.stdin.readline
    sys.setrecursionlimit(10**5)
    
    # input
    n = int(input())
    parent = [0] * (n+1)
    d = [0] * (n+1)
    visited = [False] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    dfs(1, 0)
    
    m = int(input())
    
    #output
    for _ in range(m):
        a, b = map(int, input().split())
        print(solution(a, b))