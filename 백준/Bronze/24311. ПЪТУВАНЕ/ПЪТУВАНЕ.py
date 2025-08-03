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
    
    t1, t2 = S() # hh, mm
    t3 = int(input())
    t4, t5 = S()
    br = int(input())
    t6 = int(input())
    t = timedelta(hours=t1, minutes=t2)
    tb = timedelta(minutes=t3+(t4*60)+t5+((br+1)*t6)+10)
    ans = t-tb
    total_sec = ans.total_seconds()
    if total_sec < 0:
        total_sec += 24 * 3600
    hh = int(total_sec // 3600)
    mm = int((total_sec % 3600) // 60)
    print(f"{hh:02d} {mm:02d}")
    