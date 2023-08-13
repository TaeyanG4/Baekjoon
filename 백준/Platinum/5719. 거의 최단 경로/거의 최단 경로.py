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

# https://velog.io/@j_aion/백준-5719-거의-최단-경로

def dijstra():
    distances = [INF for _ in range(n)]
    distances[s] = 0
    
    pq = []
    heappush(pq, [0, s])
    
    while pq:
        cur_cost, cur_node = heappop(pq)
        
        if distances[cur_node] < cur_cost:
            continue
        
        for next_node, next_cost in graph[cur_node]:
            # 최단 경로에 포함된 간선은 제외
            if edges[cur_node][next_node]:
                continue
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heappush(pq, [distances[next_node], next_node])
    
    return distances

def bfs():
    q = deque()
    q.append(d)
    
    while q:
        cur_node = q.popleft()
        
        if cur_node == s:
            continue
        
        for prev_node, prev_cost in graph_inv[cur_node]:
            if distances[cur_node] == distances[prev_node] + prev_cost and not edges[prev_node][cur_node]:
                # cur_node로 향하는 이전 간선 비용을 사용했을 때 distances에 기록된 비용이라면 곧 최단 경로에 사용했다는 뜻이다.
                edges[prev_node][cur_node] = True
                q.append(prev_node)
    
if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while True:
        
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        graph = defaultdict(list)
        graph_inv = defaultdict(list)
        edges = [[False for _ in range(n)] for _ in range(n)]
        s, d = map(int, input().split())

        # input
        for _ in range(m):
            u, v, p = map(int, input().split())
            graph[u].append((v, p))
            graph_inv[v].append((u, p))

        # output
        # 방향 그래프 자체를 거꾸로 만든 뒤 도착지에서 목적지로 향하면서 최단 경로가 맞는지 확인
        distances = dijstra() # 최단경로 구하기
        bfs() # 최단경로 제거
        distances = dijstra() # 거의 최단경로 구하기
        if distances[d] == INF:
            print(-1)
        else:
            print(distances[d])