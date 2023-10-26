## taeyang's template (1.0.7)
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
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    s = input().rstrip()
    
    ans = 1
    mx_d_len, mx_c_len = 0, 0
    d_len, c_len = 0, 0
    for c in s:
        if c == 'd':
            if d_len == 0:
                ans *= 10
            else:
                ans *= 9
                
            d_len += 1
            c_len = 0
        else:
            if c_len == 0:
                ans *= 26
            else:
                ans *= 25
                
            c_len += 1
            d_len = 0
    
    # output
    print(ans)