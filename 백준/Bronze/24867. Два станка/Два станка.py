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
    
    k = int(input())
    a, x = S()
    b, y = S()
    if k-a < 0:
        tmp1 = 0
    elif k-a-b < 0:
        tmp1 = (k-a)*x
    else:
        tmp1 = (k-a)*x + (k-a-b)*y
    
    if k-b < 0:
        tmp2 = 0
    elif k-a-b < 0:
        tmp2 = (k-b)*y
    else:
        tmp2 = (k-b)*y + (k-a-b)*x
    print(max(tmp1, tmp2))