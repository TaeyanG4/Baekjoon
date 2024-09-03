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
        x1, x2, y1, y2 = [*S()]
        if x1 == x2 == y1 == y2 == 0:
            break
        x_mx, x_mi, y_mx, y_mi = max(x1, x2), min(x1, x2), max(y1, y2), min(y1, y2)
        print(y_mi - x_mx, y_mx - x_mi)