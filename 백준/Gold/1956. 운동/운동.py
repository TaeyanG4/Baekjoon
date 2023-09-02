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
    dist = [[INF] * n for _ in range(n)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        dist[a-1][b-1] = d
    
    # floyd-warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # output
    print(solution(n, m, dist))