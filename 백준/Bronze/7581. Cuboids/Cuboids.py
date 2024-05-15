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

    while True:
        l, w, h, v = S() #  길이, 너비, 높이, 부피
        if l == w == h == v == 0:
            break
        if l == 0:
            l = int(v / (w * h))
        elif w == 0:
            w = int(v / (l * h))
        elif h == 0:
            h = int(v / (l * w))
        elif v == 0:
            v = int(l * w * h)
        print(l, w, h, v)