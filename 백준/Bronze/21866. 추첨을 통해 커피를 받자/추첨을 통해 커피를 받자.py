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
    
    lst = [*S()]
    if lst[0] > 100 or lst[1] > 100 or lst[2] > 200 or lst[3] > 200 or lst[4] > 300 or lst[5] > 300 or lst[6] > 400 or lst[7] > 400 or lst[8] > 500:
        print('hacker')
    elif sum(lst) >= 100:
        print('draw')
    else:
        print('none')
            