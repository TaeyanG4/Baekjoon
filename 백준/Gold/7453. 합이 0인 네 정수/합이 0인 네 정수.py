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
    n = int(input())
    lst_a, lst_b, lst_c, lst_d = [], [], [], []
    for _ in range(n):
        a, b, c, d = S()
        lst_a.append(a)
        lst_b.append(b)
        lst_c.append(c)
        lst_d.append(d)
    
    # output
    ans = 0
    lst_ab = dict()
    for a in lst_a:
        for b in lst_b:
            if a+b in lst_ab:
                lst_ab[a+b] += 1
            else:
                lst_ab[a+b] = 1
    for c in lst_c:
        for d in lst_d:
            if -c-d in lst_ab:
                ans += lst_ab[-c-d]
    print(ans)