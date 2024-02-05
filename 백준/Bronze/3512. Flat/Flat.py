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
    n, c = map(int, input().split())
    all_area = 0
    bedroom_area = 0
    pay = 0
    for _ in range(n):
        ai, ti = map(str, input().split())
        ai = int(ai)
        if ti == 'bedroom':
            bedroom_area += ai
        all_area += ai
        if ti == 'balcony':
            pay += ai/2 * c
        else:
            pay += ai * c
             
    
    # output
    print(all_area, bedroom_area, pay, sep='\n')