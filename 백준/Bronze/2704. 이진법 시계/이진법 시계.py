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
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for _ in range(int(input())):
        h, m, s = input().split(':')
        h, m, s = bin(int(h))[2:], bin(int(m))[2:], bin(int(s))[2:]
        h, m, s = h.zfill(6), m.zfill(6), s.zfill(6)
        hms_horizon = h + m + s
        hms_vertical = ''.join(''.join(x) for x in zip(h, m, s))
        print(hms_vertical, hms_horizon)