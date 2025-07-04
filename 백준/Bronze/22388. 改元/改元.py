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
    input = sys.stdin.readline
    S = lambda: map(str, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    while True:
        lst = [*S()]
        
        if lst[0] == '#':
            break
        else:
            g, y, m, d = lst
            y, m, d = int(y), int(m), int(d)
        
        if y > 31:
            print(f'? {y-30} {m} {d}')
        elif y == 31 and m >= 5:
            print(f'? {y-30} {m} {d}')
        else:
            print(f'{g} {y} {m} {d}')
