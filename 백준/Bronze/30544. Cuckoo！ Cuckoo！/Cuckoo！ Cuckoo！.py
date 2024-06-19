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
    S = lambda: map(int, input().split(':'))
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    h, m = S()
    n = int(input())
    if m == 0:
        n -= h
    elif m % 15 == 0:
        n -= 1
    while True:
        if n <= 0:
            break
        m = ((m // 15) + 1) * 15
        if m == 60:
            h += 1
            m = 0
            if h > 12:
                h = 1
            n -= h
        else:
            n -= 1
    if m == 0:
        m = '00'
    if h <= 9:
        h = '0' + str(h)
    print(f'{h}:{m}')