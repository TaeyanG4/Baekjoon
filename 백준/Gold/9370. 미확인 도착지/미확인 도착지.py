## taeyang's template (1.0.1)
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
from collections import *
from heapq import *
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
#################################

def dijkstra(graph, start, end):
    dist = [INF] * (n + 1)
    dist[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        d, now = heappop(q)
        if dist[now] < d:
            continue
        for nx, nd in graph[now]:
            cost = d + nd
            if cost < dist[nx]:
                dist[nx] = cost
                heappush(q, (cost, nx))
    return dist

def solution(graph, n, m, t, s, g, h, x, gh_dist):
    # n = 교차로의 개수
    # m = 도로의 개수
    # t = 목적지 후보의 개수
    # s = 예술가의 출발지
    # g, h = 예술가가 지나간 도로
    # x = 목적지 후보
    
    ans = []
    for v in x:
        dist = dijkstra(graph, s, v)
        
        sg_dist = dijkstra(graph, s, g)
        hv_dist = dijkstra(graph, h, v)
        if dist[v] == (sg_dist[g] + gh_dist + hv_dist[v]):
            ans.append(v)
            continue
        
        sh_dist = dijkstra(graph, s, h)
        gv_dist = dijkstra(graph, g, v)
        if dist[v] == (sh_dist[h] + gh_dist + gv_dist[v]):
            ans.append(v)

    return sorted(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    T = int(input())
    
    # output
    for _ in range(T):
        graph = defaultdict(list)
        n, m, t = map(int, input().split())
        s, g, h = map(int, input().split())
        for _ in range(m):
            a, b, d = map(int, input().split())
            graph[a].append((b, d))
            graph[b].append((a, d))
            if (a == g and b == h) or (a == h and b == g):
                gh_dist = d
        x = [int(input()) for _ in range(t)]
        print(*solution(graph, n, m, t, s, g, h, x, gh_dist))