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

def solution():
    for i in range(2, n+1):
        way1, way2, way3 = INF, INF, INF
        if i%3==0:
            way1 = memo[i//3]
        if i%2==0:
            way2 = memo[i//2]
        way3 = memo[i-1]
        
        if min(way1, way2, way3) == way1:
            memo[i] = way1 + 1
            graph[i] = i//3
        elif min(way1, way2, way3) == way2:
            memo[i] = way2 + 1
            graph[i] = i//2
        else:
            memo[i] = way3 + 1
            graph[i] = i-1
    
    return memo

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    memo = [0] * (n+1)
    graph = defaultdict(int)
    
    # output
    solution()
    print(memo[n])
    while n != 0:
        print(n, end=' ')
        n = graph[n]