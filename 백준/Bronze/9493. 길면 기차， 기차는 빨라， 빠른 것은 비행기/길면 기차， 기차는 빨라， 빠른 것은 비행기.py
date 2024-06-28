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
        m, a, b = S()
        if m == a == b == 0:
            break
        at, bt = m/a, m/b
        sec = int(round(abs(at-bt)*3600, 0))
        h = sec // 3600
        mm = sec % 3600 // 60
        ss = sec % 60
        print(f'{h}:{mm:02}:{ss:02}')