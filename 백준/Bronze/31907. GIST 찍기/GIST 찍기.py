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
from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
# getcontext().prec = 20
#################################

def solution():
    pass

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    
    n = int(input())
    board = [['.' for _ in range(n*4)] for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            board[i][j] = 'G'
    for i in range(n*1, n*2):
        for j in range(n*1, n*2):
            board[i][j] = 'I'
    for i in range(n*2, n*3):
        for j in range(n*2, n*3):
            board[i][j] = 'S'
    for i in range(n, n*2):
        for j in range(n*3, n*4):
            board[i][j] = 'T'
    for line in board:
        print(''.join(line))
    