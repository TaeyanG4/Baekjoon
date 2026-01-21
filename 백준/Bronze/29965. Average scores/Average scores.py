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
    # input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    n = int(input())
    m, j = 0, 0
    mm, jj = 0, 0
    for i in range(n):
        a, b = map(str, input().split())
        if a == 'M':
            m += int(b)
            mm += 1
        else:
            j += int(b)
            jj += 1
    if m == 0 and j == 0:
        print('V')
    elif m == 0:
        print('J')
    elif j == 0:
        print('M')
    else:
        if m/mm > j/jj:
            print('M')
        elif m/mm < j/jj:
            print('J')
        else:
            print('V')