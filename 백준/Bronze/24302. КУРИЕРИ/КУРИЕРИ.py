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
from decimal import *
getcontext().prec = 20
#################################


def delivery1_st(x):

    if x <= 5:
        return 400
    elif x <= 10:
        return 700
    elif x <= 20:
        return 1200
    elif x <= 30:
        return 1700
    else:
        return x * 57

def delivery2_st(x):
    
    if x <= 2:
        return 90 + x * 90
    elif x <= 5:
        return 100 + x * 85
    elif x <= 20:
        return 125 + x * 80
    elif x <= 40:
        return 325 + x * 70
    else:
        return 925 + x * 55

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    a, b = S()
    a = a//1000
    b = b//1000
    cost_a = min(delivery1_st(a), delivery2_st(a))
    cost_b = min(delivery1_st(b), delivery2_st(b))
    lv, st = divmod(cost_a + cost_b, 100)
    print(f"{lv}.{st:02d}")