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
# from collections import *
# from itertools import *
# from statistics import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

def solution(n, m, mat):
    for i  in range(n):
        for j in range(m):
            di, dj = directions[mat[i][j]]
            ny, nx = i + di, j + dj
            union(i*m + j, ny*m + nx)
    
    return len(set(find(i) for i in range(n*m)))

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    # INF = sys.maxsize
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    mat = [list(input().strip()) for _ in range(n)]
    parents = [i for i in range(n*m)]
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    
    # output
    print(solution(n, m, mat))