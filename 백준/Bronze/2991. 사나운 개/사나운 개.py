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
# from functools import *
#################################


def solution():
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # input
    a, b, c, d = map(int, input().split())
    p, m, n = map(int, input().split())
    pa, pm, pn = 0, 0, 0
    
    # output
    if p%(a+b) <= a and p%(a+b) != 0:
        pa += 1
    if p%(c+d) <= c and p%(c+d) != 0:
        pa += 1
    if m%(a+b) <= a and m%(a+b) != 0:
        pm += 1
    if m%(c+d) <= c and m%(c+d) != 0:
        pm += 1
    if n%(a+b) <= a and n%(a+b) != 0:
        pn += 1
    if n%(c+d) <= c and n%(c+d) != 0:
        pn += 1
        
    print(pa)
    print(pm)
    print(pn)