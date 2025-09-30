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
    
    hh1, mm1 = map(int, input().split(':'))
    mm2, ss2 = hh1, mm1
    t1 = timedelta(hours=hh1, minutes=mm1)
    t2 = timedelta(minutes=mm2, seconds=ss2)
    ans = t1 - t2
    total= ans.days * 24 * 3600 + ans.seconds
    h = total // 3600
    m = (total%3600) // 60
    s = total%60
    print(f"{h:02}:{m:02}:{s:02}")