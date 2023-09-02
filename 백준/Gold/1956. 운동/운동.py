## taeyang's template (1.0.3)
#################################
## my import lines
import sys
# import math
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

def floyd_warshall(n):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def solution(n, m, dist):
    
    ans = INF
    for i in range(n):
        ans = min(ans, dist[i][i])
    return -1 if ans == INF else ans

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    dist = [[INF] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        dist[a][b] = d
    floyd_warshall(n)

    # output
    print(solution(n, m, dist))