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

    # input
    n = int(input())
    lst = [*map(int, input().split())]
    
    if n < 5:
        for i in range(5 - n):
            lst.append(0)
    
    if lst[0] > lst[2]:
        tmp1 = (lst[0] - lst[2]) * 508
    else:
        tmp1 = (lst[2] - lst[0]) * 108
        
    if lst[1] > lst[3]:
        tmp2 = (lst[1] - lst[3]) * 212
    else:
        tmp2 = (lst[3] - lst[1]) * 305
        
    tmp3 = lst[4] * 707
    
    # output
    print((tmp1 + tmp2 + tmp3) * 4763)