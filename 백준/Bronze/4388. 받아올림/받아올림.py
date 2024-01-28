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

    
    while True:
        # input
        a, b = map(str, input().split())
        if a == '0' and b == '0':
            break
        if int(a) < int(b):
            a, b = b, a
        a, b = list(a), list(b)
        ans, tmp = 0, 0
        while len(a) != 0 or len(b) != 0:
            if len(b) == 0:
                i , j = int(a.pop()), 0
            else:
                i, j = int(a.pop()), int(b.pop())
              
            if i + j + tmp >= 10:
                ans += 1
                tmp = 1
            else:
                tmp = 0
        
        # output
        print(ans)
