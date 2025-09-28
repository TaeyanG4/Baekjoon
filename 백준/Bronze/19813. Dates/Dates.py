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
    
    for i in range(int(input())):
        s = input().rstrip()
        if '.' in s:
            d, m, y = s.split('.')
        else:
            m, d, y = s.split('/')
        d, m, y = int(d), int(m), int(y)
        print(f"{d:02d}.{m:02d}.{y:04d} {m:02d}/{d:02d}/{y:04d}")