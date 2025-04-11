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
    
    mx = -INF
    ans = 0
    for i in range(3):
        a, b = S()
        if a*10 >= 5000:
            tmp = (b*10)/(a*10-500)
        else:
            tmp = b/a
        if mx < tmp:
            mx = tmp
            ans = i
    if ans == 0:
        print('S')
    elif ans == 1:
        print('N')
    else:
        print('U')