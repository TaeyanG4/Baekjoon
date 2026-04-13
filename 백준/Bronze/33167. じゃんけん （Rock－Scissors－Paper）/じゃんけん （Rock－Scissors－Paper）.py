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
    lst_a = input().rstrip()
    lst_b = input().rstrip()
    a, b = 0, 0
    for i, j in zip(lst_a, lst_b):

        if i == 'R' and j == 'S':
            a += 1
        elif i == 'S' and j == 'R':
            b += 1
        elif i == 'P' and j == 'R':
            a += 1
        elif i == 'R' and j == 'P':
            b += 1
        elif i == 'S' and j == 'P':
            a += 1
        elif i == 'P' and j == 'S':
            b += 1
    print(a, b)