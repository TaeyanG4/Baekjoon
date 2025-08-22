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
    
    
    b, c, d, legs = S()
    ans = []
    cnt = 0
    for i in range(legs//b+1):
        if i*b > legs:
            break
        for j in range(legs//c+1):
            if i*b + j*c> legs:
                    break
            for k in range(legs//d+1):
                if i*b + j*c + k*d > legs:
                    break
                if i*b + j*c + k*d == legs:
                    print(i, j, k)
                    cnt += 1
    if cnt == 0:
        print("impossible")
