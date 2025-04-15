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
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    m, s, x1, x2 = S()

    # X1 = (a × Seed + c) % m
    # X2 = (a × X1 + c) % m
    for i in range(m + 1):
        for j in range(m + 1):
            if x1 == (i * s + j) % m and x2 == (i * x1 + j) % m:
                print(i, j)
                exit(0)