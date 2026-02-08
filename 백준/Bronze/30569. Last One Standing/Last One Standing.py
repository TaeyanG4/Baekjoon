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
# getcontext().prec = 20
#################################

def solution():
    pass


if __name__ == "__main__":
    # input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    h1, d1, t1 = S()
    h2, d2, t2 = S()
    h1 -= d2
    h2 -= d1
    tmp1 = math.ceil(h2/d1)*t1
    tmp2 = math.ceil(h1/d2)*t2
    if tmp1 == tmp2:
        print("draw")
    elif tmp1 < tmp2:
        print("player one")
    else:
        print("player two")