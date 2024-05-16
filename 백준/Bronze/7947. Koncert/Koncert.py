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

    for _ in range(int(input())):
        rc, gc, bc = 0, 0, 0
        for _ in range(10):
            a, b, c = S()
            rc += a
            gc += b
            bc += c
        rc /= 10
        gc /= 10
        bc /= 10
        if rc % 1 >= 0.5:
            rc += 1
            rc = int(rc)
        else:
            rc = int(rc)
        if gc % 1 >= 0.5:
            gc += 1
            gc = int(gc)
        else:
            gc = int(gc)
        if bc % 1 >= 0.5:
            bc += 1
            bc = int(bc)
        else:
            bc = int(bc)
        print(rc, gc, bc)