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

    # input
    lst = [*map(int, input().split())]
    flag = True
    for i in combinations(lst, 2):
        if flag:
            res = i[0] or i[1]
            flag = False
        else:
            tmp = i[0] or i[1]
            if res == tmp:
                res = False
            else:
                res = True
    for i in combinations(lst, 3):
        tmp = i[0] or i[1] or i[2]
        if res == tmp:
            res = False
        else:
            res = True
    
    # output
    if res:
        print(1)
    else:
        print(0)