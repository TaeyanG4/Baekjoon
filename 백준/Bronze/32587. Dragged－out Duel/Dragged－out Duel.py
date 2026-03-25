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
    me, guile = input().rstrip(), input().rstrip()
    m, g = 0, 0
    for i, j in zip(me, guile):
        if i == 'R' and j == 'S':
            m += 1
        elif i == 'S' and j == 'R':
            g += 1
        elif i == 'P' and j == 'R':
            m += 1
        elif i == 'R' and j == 'P':
            g += 1
        elif i == 'S' and j == 'P':
            m += 1
        elif i == 'P' and j == 'S':
            g += 1
    print('victory' if m > g else 'defeat')
    
    