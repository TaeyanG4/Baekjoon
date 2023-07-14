# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################

def solution(n, m, ind, graph):
    res = []
    q = deque()
    for i in range(1, n + 1):
        if ind[i] == 0:
            q.append(i)
    
    while q:
        cur = q.popleft()
        res.append(cur)
        for nxt in graph[cur]:
            ind[nxt] -= 1
            if ind[nxt] == 0:
                q.append(nxt)
    return res

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n, m = map(int, input().split())
    ind = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        li = list(map(int, input().split()))
        for j in range(1, li[0]):
            graph[li[j]].append(li[j + 1])
            ind[li[j + 1]] += 1
    
    # output
    ans = solution(n, m, ind, graph)
    if len(ans) != n:
        print(0)
    else:
        for i in ans:
            print(i)