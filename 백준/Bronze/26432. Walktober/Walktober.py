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
        m, n, p = S()
        p_lst = []
        ans = 0
        for j in range(m):
            lst = list(S())
            if j != p-1:
                p_lst.append(lst)
            else:
                my_lst = lst
                le = len(my_lst)
        for k, v in enumerate(zip(*p_lst)):
            mx = max(v)
            if my_lst[k] < mx:
                ans += mx - my_lst[k]
        print(f'Case #{i+1}: {ans}')