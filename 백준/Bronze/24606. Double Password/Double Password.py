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
    
    s1 = input().strip()
    s2 = input().strip()
    ans = 0
    for i, j in zip(s1, s2):
        if i == j:
            ans += 1
    if ans == 4:
        print(1)
    elif ans == 3:
        print(2)
    elif ans == 2:
        print(4)
    elif ans == 1:
        print(8)
    else:
        print(16)