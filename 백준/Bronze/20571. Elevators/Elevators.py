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
    S = lambda: map(str, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    s, n = S()
    n = int(n)
    if s == 'residential':
        if n == 1:
            print(0)
        elif 2 <= n <= 5:
            print(1)
        elif 6 <= n <= 10:
            print(2)
        elif 11 <= n <= 15:
            print(3)
        else:
            print(4)
    elif s == 'commercial':
        if n == 1:
            print(0)
        elif 2 <= n <= 7:
            print(1)
        elif 8 <= n <= 14:
            print(2)
        elif 15 <= n <= 20:
            print(3)
    else:
        if n == 1:
            print(0)
        elif 2 <= n <= 4:
            print(1)
        elif 5 <= n <= 8:
            print(2)
        elif 9 <= n <= 12:
            print(3)
        elif 13 <= n <= 16:
            print(4)
        else:
            print(5)