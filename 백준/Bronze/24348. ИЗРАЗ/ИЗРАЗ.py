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
from itertools import *
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
    
    a, b, c = S()
    cal = ['+', '-', '*']
    comb_cal = list(permutations(cal, 2))
    abc_perm = list(permutations([a, b, c], 3))
    ans = -INF
    for i, j in comb_cal:
        for k, l, m in abc_perm:
            ans = max(ans, eval(f"{k}{i}{l}{j}{m}"))
    print(ans)