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
    p, q = map(int, input().split())
    
    # 두수의 최소 공약수
    lst_p, lst_q = [], []
    for i in range(1, int(math.sqrt(p)) + 1):
        if p % i == 0:
            lst_p.append(i)
            lst_p.append(p // i)
    for i in range(1, int(math.sqrt(q)) + 1):
        if q % i == 0:
            lst_q.append(i)
            lst_q.append(q // i)
    lst_p = sorted(list(set(lst_p)))
    lst_q = sorted(list(set(lst_q)))

    # output
    for i, j in product(lst_p, lst_q):
        print(i, j)