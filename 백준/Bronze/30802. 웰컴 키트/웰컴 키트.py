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
    s, m, l, xl, xxl, xxxl = S()
    t, p = S()
    
    ans_t = 0
    for i in [s, m, l, xl, xxl, xxxl]:
        ans_t += math.ceil(i / t)
    print(ans_t)
    print(sum([s, m, l, xl, xxl, xxxl]) // p, sum([s, m, l, xl, xxl, xxxl]) % p)