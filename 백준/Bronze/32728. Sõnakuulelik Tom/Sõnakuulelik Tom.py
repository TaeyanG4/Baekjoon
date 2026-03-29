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
    
    n, k = S()
    s = input().strip()
    b1, b2, b3 = [], [], []
    for c in s:
        if c == 's':
            if len(b1) < k:
                b1.append(c)
            elif len(b2) < k:
                b2.append(c)
            elif len(b3) < k:
                b3.append(c)
        elif c == 'r':
            if len(b2) < k:
                b2.append(c)
            elif len(b3) < k:
                b3.append(c)
            elif len(b1) < k:
                b1.append(c)
        elif c == 'p':
            if len(b3) < k:
                b3.append(c)
            elif len(b1) < k:
                b1.append(c)
            elif len(b2) < k:
                b2.append(c)
    print(''.join(b1))
    print(''.join(b2))
    print(''.join(b3))
        
    