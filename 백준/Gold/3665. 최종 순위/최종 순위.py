## taeyang's template (1.0.7)
# https://hongcoding.tistory.com/96
# https://my-coding-notes.tistory.com/307
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


def topological_sort():
    
    res = []
    q = deque()
    for i in range(1, n + 1):
        if ind[i] == 0:
            q.append(i) # 진입 차수가 0인 노드를 큐에 삽입
    
    while q:
        tmp = q.popleft()
        res.append(tmp)
        for node in graph[tmp]:
            ind[node] -= 1
            if ind[node] == 0:
                q.append(node)
    
    return res


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    # n, m = map(int, input().split())
    t = int(input())
    for _ in range(t):
        
        # input
        n = int(input())
        lst = [*map(int, input().split())] 
        m = int(input())
        
        # default setting
        graph = defaultdict(list)
        ind = [0] * (n + 1)
        for i in range(n):
            graph[lst[i]].extend(lst[i+1:])
            ind[lst[i]] += i
        
        for _ in range(m):
            a, b = S()
            if b in graph[a]:
                graph[a].remove(b)
                graph[b].append(a)
                ind[a] += 1
                ind[b] -= 1
            else:
                graph[b].remove(a)
                graph[a].append(b)
                ind[b] += 1
                ind[a] -= 1

        # output
        ans = topological_sort()
        if sum(ind) != 0:
            print("IMPOSSIBLE")
        else:
            print(*ans)
