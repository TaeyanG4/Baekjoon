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
from collections import *
# from heapq import *
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

    n = int(input())
    for i in range(n):
        ug, us, ub, rg, rs, rb = S()
        print(ug, us, ub, rg, rs, rb)
        color, count = False, False
        u = ug+us+ub
        r = rg+rs+rb
        
        
        if u > r:
            count = True
        if ug > rg:
            color = True
        elif ug == rg:
            if us > rs:
                color = True
            elif us == rs:
                if ub > rb:
                    color = True
        if color and count:
            print("both")
        elif color:
            print("color")
        elif count:
            print("count")
        else:
            print("none")
        print()