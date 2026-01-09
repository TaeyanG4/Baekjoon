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
    # input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    
    g, gb, y, r, ry = S()
    t = int(input())
    cycle = g + gb + y + r + ry
    q, rem = divmod(t, cycle)
    rr_c, yy_c, gg_c = r+ry, y+ry, g+gb//2
    rr, yy, gg = q*rr_c, q*yy_c, q*gg_c
    if rem > 0:
        d = min(rem, g)
        gg += d
        rem -= d
    if rem > 0:
        d = min(rem, gb)
        gg += d//2
        rem -= d
    if rem > 0:
        d = min(rem, y)
        yy += d
        rem -= d
    if rem > 0:
        d = min(rem, r)
        rr += d
        rem -= d
    if rem > 0:
        d = min(rem, ry)
        rr += d
        yy += d
        rem -= d
    print(rr, yy, gg)