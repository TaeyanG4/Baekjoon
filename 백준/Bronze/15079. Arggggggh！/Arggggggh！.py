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
    S = lambda: map(str, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    n = int(input())
    x, y = map(int, input().split())
    for _ in range(n-1):
        c, d = S()
        d = int(d)
        if c == 'N':
            y += d
        elif c == 'S':
            y -= d
        elif c == 'E':
            x += d
        elif c == 'W':
            x -= d
        elif c == 'NE':
            x += (d**2/2) ** 0.5
            y += (d**2/2) ** 0.5
        elif c == 'NW':
            x -= (d**2/2) ** 0.5
            y += (d**2/2) ** 0.5
        elif c == 'SE':
            x += (d**2/2) ** 0.5
            y -= (d**2/2) ** 0.5
        elif c == 'SW':
            x -= (d**2/2) ** 0.5
            y -= (d**2/2) ** 0.5
    print(x, y)