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
    S = lambda: map(float, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # input
    k = int(input())
    for i in range(k):
        b, w = S()
        b = int(b)
        
        tmp = 0 
        for _ in range(b):
            ri = float(input())
            if ri == 0:
                continue
            tmp += 4/3 * math.pi * (ri**3) / 1000
        
        # output
        print(f'Data Set {i+1}:')
        if tmp >= w:
            print('Yes')
        else:
            print('No')
        print()