## taeyang's template (1.0.4)
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
    # n, m = map(int, input().split())
    # li = [*map(int, input().split())]
    a, b, c = int(input()), int(input()), int(input())
    mi, mx = min(a, b), max(a, b)
    
    # output
    if mi/c >= 2 and mi/mx <= 2:
        print('good')
    else:
        print('bad')
