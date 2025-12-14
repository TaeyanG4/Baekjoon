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
    # input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    mi = INF
    n, m = S()
    x, y = -1, -1
    for i in range(n):
        lst = [*S()]
        for j in range(m):
            if (i+1)+abs((m+1)/2-(j+1)) < mi and lst[j] == 0:
                mi = min(mi, (i+1)+abs((m+1)/2-(j+1)))
                x, y = i+1, j+1
    if x == -1:
        print(-1)
    else:
        print(x, y)