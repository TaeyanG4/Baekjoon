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
    S = lambda: map(str, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    ans = 0
    for _ in range(int(input())):
        lst = [*S()]
        if lst[0] == 'S':
            r = float(lst[1])
            tmp = math.pi*(4/3)*(r**3)
        elif lst[0] == 'C':
            r, h = float(lst[1]), float(lst[2])
            tmp = math.pi*r**2*h
        else:
            r, h = float(lst[1]), float(lst[2])
            tmp = math.pi*r**2*h/3
        ans = max(ans, tmp)
    print(f'{ans:.3f}')