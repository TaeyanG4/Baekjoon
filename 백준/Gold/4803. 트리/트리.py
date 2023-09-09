## taeyang's template (1.0.4)
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
# from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]
    
def solution():
    
    cycle = []
    for _ in range(m):
        a, b = map(int, input().split())
        if find(a) != find(b):
            union(a, b)
        else:
            cycle.append(a)

    for i in range(1, n + 1):
        find(i)
        
    group = set()
    for v in cycle:
        group.add(parents[v])
        
    ans = 0
    for i in range(1, n + 1):
        if parents[i] in group:
            continue
        ans += 1
        group.add(parents[i])

    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    cnt = 1
    while True:
        
        # input
        n, m = map(int, input().split())
        
        if n == 0 and m == 0:
            break
        
        # output
        parents = [i for i in range(n + 1)]
        ans = solution()
        if ans == 0:
            print(f'Case {cnt}: No trees.')
        elif ans == 1:
            print(f'Case {cnt}: There is one tree.')
        else:
            print(f'Case {cnt}: A forest of {ans} trees.')
            
        cnt += 1