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

def solution(n, m, r, t, mat):
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    mat[i][j] = 0
                if mat[i][k]+mat[k][j] > m:
                    continue
                mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j])
                
    max_item = []
    for i in range(1, n+1):
        temp = 0
        for j in range(1, n+1):
            if mat[i][j] <= m:
                temp += t[j-1]
        max_item.append(temp)
    return max(max_item)

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n, m, r = map(int, input().split())
    t = list(map(int, input().split()))
    # graph = defaultdict(list)
    mat = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(r):
        u, v, w = map(int, input().split())
        # graph[u].append((v, w))
        # graph[v].append((u, w))
        mat[u][v] = w
        mat[v][u] = w
    
    # output
    print(solution(n, m, r, t, mat))
