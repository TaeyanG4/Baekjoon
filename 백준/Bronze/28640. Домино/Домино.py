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

    a1, a2 = input().split('|')
    b1, b2 = input().split('|')
    a1, a2 = len(a1), len(a2)-1
    b1, b2 = len(b1), len(b2)-1
    if a1 == b1 or a1 == b2 or a2 == b1 or a2 == b2:
        print("Yes")
    else:
        print("No")