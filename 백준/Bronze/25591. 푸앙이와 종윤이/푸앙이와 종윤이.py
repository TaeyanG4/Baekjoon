## taeyang's template (1.0.5)
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

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    # lst = [*map(int, input().split())]
    i, j = map(int, input().split())
    a = 100 - i
    b = 100 - j
    c = 100 - (a + b)
    d = a * b
    q, r = divmod(d, 100)
    
    # output
    print(a, b, c, d, q, r)
    print(c+q, r)