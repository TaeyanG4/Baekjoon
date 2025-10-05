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


def push(v):
    heappush(left, -v)
    if right and (-left[0] > right[0]):
        heappush(right, -heappop(left))
    if len(left) > len(right)+1:
        heappush(right, -heappop(left))
    if len(right) > len(left):
        heappush(left, -heappop(right))

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    t = int(input())
    for i in range(t):
        n = int(input())
        lst = []
        for i in range((n+9)//10):
            lst.extend(S())
        ans = []
        left, right = [], []
        for i, v in enumerate(lst):
            push(v)
            if i % 2 == 0:
                ans.append(-left[0])
        print(len(ans))
        for i in range(0, len(ans), 10):
            print(*ans[i:i+10])