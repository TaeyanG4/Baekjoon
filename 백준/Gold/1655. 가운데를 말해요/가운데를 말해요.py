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
from heapq import *
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
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    mid = None
    left, right = [], []
    for i in range(int(input())):
        n = int(input())
        
        if len(left) == len(right):
            heappush(left, -n)
        else:
            heappush(right, n)
        
        if right and -left[0] > right[0]:
            a = -heappop(left)
            b = heappop(right)
            heappush(left, -b)
            heappush(right, a)
        
        print(-left[0])
                