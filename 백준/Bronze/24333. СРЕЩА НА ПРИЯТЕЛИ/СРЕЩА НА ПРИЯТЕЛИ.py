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
from datetime import *
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
    
    l1, r1, l2, r2, k = S()
    if l1 > l2 and r1 > r2:
        l1, r1, l2, r2 = l2, r2, l1, r1
    mx_s, mi_e = max(l1, l2), min(r1, r2)
    if mx_s <= k <= mi_e:
        ans = mi_e - mx_s
    else:
        ans = mi_e - mx_s + 1   
    if ans < 0:
        ans = 0
    print(ans)