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

    q1, q2, q3, q4, axis = 0, 0, 0, 0, 0
    for _ in range(int(input())):
        x, y = S()
        if x > 0 and y > 0:
            q1 += 1
        elif x < 0 and y > 0:
            q2 += 1
        elif x < 0 and y < 0:
            q3 += 1
        elif x > 0 and y < 0:
            q4 += 1
        else:
            axis += 1
    print("Q1:", q1)
    print("Q2:", q2)
    print("Q3:", q3)
    print("Q4:", q4)
    print("AXIS:", axis)