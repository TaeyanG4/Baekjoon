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

def solution():
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    route_save[i][j] = route_save[i][k] + route_save[k][j][1:]

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = int(input()), int(input())
    graph = [[INF] * n for _ in range(n)]
    route_save = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        if graph[a-1][b-1] > c:
            graph[a-1][b-1] = c
            route_save[a-1][b-1] = [a, b]
    
    # output
    solution()
    
    for line in graph:
        for e in line:
            if e == INF:
                print(0, end=' ')
            else:
                print(e, end=' ')
        print()
        
    for line in route_save:
        for e in line:
            if not e:
                print(0)
            else:
                print(len(e), *e)