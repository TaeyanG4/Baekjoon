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

    p1, p2, p3 = S()
    c1, c2, c3 = S()
    lst = sorted([p1, p2, p3], reverse=True)
    c1_v = sum(lst)*(c1/100)
    if c2 < c3:
        c2, c3 = c3, c2
    c2c3_v = (lst[0]*(c2/100)) + (lst[1]*(c3/100))
    if c1_v > c2c3_v:
        print(f'one {c1_v:.2f}')
    else:
        print(f'two {c2c3_v:.2f}')