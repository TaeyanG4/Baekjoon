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
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
#################################

def solution(graph, start):
    q = deque()
    q.append(start)
    visited[start] = 1
    
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = -1 * visited[cur]
            elif visited[nxt] == visited[cur]:
                return False
            
    return True

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    t = int(input())
    
    # output
    for _ in range(t):
        graph = defaultdict(list)
        v, e = map(int, input().split())
        for _ in range(e):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        visited = [0] * (v + 1)
        
        for i in range(1, v + 1):
            if not visited[i]:
                ans = solution(graph, i)
                if not ans:
                    break
            
        print('YES' if ans else 'NO')