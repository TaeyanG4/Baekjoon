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
from collections import *
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
    a, b = sorted(S()), sorted(S())
    
    wina = 0
    j = 0
    for i in a:
        while j < n and b[j] < i:
            j += 1
        wina += j
    ca = Counter(a)
    cb = Counter(b)
    ties = sum(ca[v] * cb.get(v, 0) for v in ca)
    total = n**2
    winb = total - wina - ties
    if wina > winb:
        print("first")
    elif wina < winb:
        print("second")
    else:
        print("tie")
    
    