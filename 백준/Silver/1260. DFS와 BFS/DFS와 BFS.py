# import line
import sys
import math
import copy
import ast
import re
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *

# 재귀함수를 이용한 DFS 구현
def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')
    for next in range(1, len(graph)):
        if not visited[next] and graph[v][next]:
            dfs(graph, visited, next)

# 큐를 이용한 BFS 구현
def bfs(graph, visited, v):
    q = [v]
    visited[v] = True
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for next in range(1, len(graph)):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)

# def sol(l):
#     pass

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n, m ,v = map(int, input().split())
    graph = [[False]*(n+1) for _ in range(n+1)]
    visited_dfs, visited_bfs = [False]*len(graph), [False]*len(graph)
    
    ## graph info
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = True
        graph[b][a] = True
    
    # Output
    dfs(graph, visited_dfs, v)
    print()
    bfs(graph, visited_bfs, v)