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
    
    a, b = input().strip(), input().strip()
    if len(a) != len(b):
        if len(a) > len(b):
            b = b.zfill(len(a))
        else:
            a = a.zfill(len(b))
    ans = ''
    for i, j in zip(a, b):
        if (int(i) <= 2 and int(j) <= 2) or (int(i) >= 7 and int(j) >= 7):
            ans += '0'
        else:
            ans += '9'
    print(ans)