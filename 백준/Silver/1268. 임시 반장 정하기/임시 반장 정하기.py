## taeyang's template (1.0.8)
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
# from functools import *
#################################


def solution():
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    clas = [[0] * n for _ in range(n)]
    for grade in range(5):
        for i in range(n):
            for j in range(i+1, n):
                if board[i][grade] == board[j][grade]:
                    clas[i][j] = clas[j][i] = 1
                    
    ans = []
    for i in clas:
        ans.append(i.count(1))
        
    print(ans.index(max(ans)) + 1)