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

    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    n = int(input())
    if a == b == c == d:
        print(1)
    elif a == b == c:
        if a - d == n:
            print(1)
        else:
            print(0)
    elif a == b == d:
        if a - c == n:
            print(1)
        else:
            print(0)
    elif a == c == d:
        if a - b == n:
            print(1)
        else:
            print(0)
    elif b == c == d:
        if b - a == n:
            print(1)
        else:
            print(0)
    else:
        print(0)
        