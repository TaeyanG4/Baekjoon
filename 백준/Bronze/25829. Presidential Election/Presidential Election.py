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
    
    n1, n2, e1, e2 = 0, 0, 0, 0
    for i in range(int(input())):
        e, v1, v2 = S()
        n1 += v1
        n2 += v2
        if v1 > v2:
            e1 += e
        elif v1 < v2:
            e2 += e
    if n1 > n2 and e1 > e2:
        print(1)
    elif n1 < n2 and e1 < e2:
        print(2)
    else:
        print(0)
    