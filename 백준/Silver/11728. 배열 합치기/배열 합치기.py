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

    n, m = S()
    lst_a, lst_b = sorted(S()), sorted(S())
    lst = []
    a_p, b_p = 0, 0
    while True:
        if a_p == n:
            lst.extend(lst_b[b_p:])
            break
        if b_p == m:
            lst.extend(lst_a[a_p:])
            break
        if lst_a[a_p] < lst_b[b_p]:
            lst.append(lst_a[a_p])
            a_p += 1
        else:
            lst.append(lst_b[b_p])
            b_p += 1
    print(*lst)