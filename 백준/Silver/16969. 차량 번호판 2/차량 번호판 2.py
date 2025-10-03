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
    MOD = 10**9 + 9
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    num, alp = 10, 26
    s = input().rstrip()
    ans = 1
    tmp = ''
    for c in s:
        if c == 'd':
            ans *= num-1 if tmp == 'd' else num
        else:
            ans *= alp-1 if tmp == 'c' else alp
        ans %= MOD
        tmp = c
    print(ans)