## taeyang's template (1.0.7)
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
from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################


def backtracking(graph):
    global ans
    sm = 0
    for i in range(n):
        if board[graph[i]][graph[i+1]] == 0:
            return
        sm += board[graph[i]][graph[i+1]]
    ans = min(ans, sm)


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    n = int(input())
    board = [[*map(int, input().split())] for _ in range(n)]
    ans = INF
    
    # backtracking
    for combi in permutations(list(range(n))):
        backtracking(list(combi)+[combi[0]])
    
    # output
    print(ans)