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

    bx, by = S()
    dx, dy = S()
    xx, yy = S()
    bes, dai = max(abs(bx-xx), abs(by-yy)), abs(dx-xx)+abs(dy-yy)
    if bes > dai:
        print("daisy")
    elif bes < dai:
        print("bessie")
    else:
        print("tie")
