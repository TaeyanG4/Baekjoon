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

    # input
    t = int(input())
    
    # output
    for _ in range(t):
        a1, p1 = S()
        r1, p2 = S()
        slicepizza = a1 / p1
        cirularpizza = (math.pi * r1 * r1) / p2
        if slicepizza > cirularpizza:
            print("Slice of pizza")
        else:
            print("Whole pizza")