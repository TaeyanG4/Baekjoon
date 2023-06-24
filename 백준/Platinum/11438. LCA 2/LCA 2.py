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
# from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

# youtu.be/O895NbxirM8
# https://bbbyung2.tistory.com/75
# https://bbbyung2.tistory.com/76

def dfs(x, depth):
    visited[x] = True
    level[x] = depth
    for node in graph[x]:
        if not visited[node]:
            parent[node][0] = x
            dfs(node, depth+1)

# 모든 노드의 2^i번째 부모 노드를 찾는다.
def set_parent():
    dfs(1, 0)
    for i in range(1, int(math.log2(n))+1):
        for j in range(1, n+1):
            # 각 노드의 2^i번째 부모 노드는 2^(i-1)번째 부모 노드의 2^(i-1)번째 부모 노드와 같다.
            parent[j][i] = parent[parent[j][i-1]][i-1]

def solution(a, b):
    # lca
    
    if level[a] > level[b]:
        a, b = b, a
    
    for i in range(int(math.log2(n)), -1, -1):
        if level[b] - level[a] >= 2**i:
            b = parent[b][i]
    
    if a == b:
        return a
    
    for i in range(int(math.log2(n)), -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    
    return parent[a][0]

if __name__ == '__main__':
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)
    
    # input
    n = int(input())
    parent = [[0] * int(math.log2(n)+1) for _ in range(n+1)]
    level = [0] * (n+1)
    visited = [False] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    set_parent()
    
    m = int(input())
    
    #output
    for _ in range(m):
        a, b = map(int, input().split())
        print(solution(a, b))