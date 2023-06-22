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
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        ind[b] += 1
    
    for i in range(1, n+1):
        if ind[i] == 0:
            res.append(i)
            q.append(i)

    while q:
        tmp = q.popleft()
        for i in graph[tmp]:
            ind[i] -= 1
            if ind[i] == 0:
                res.append(i)
                q.append(i)
    return res

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n, m = map(int, input().split()) 
    ind = [0] * (n+1)
    graph = [[] for _ in range(n+1)] 
    
    # output
    print(*solution(n, m, ind, graph))