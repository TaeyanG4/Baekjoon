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

    x1, y1, x2, y2 = S()
    x3, y3, x4, y4 = S()
    xmi, xmx = min(x1, x2, x3, x4), max(x1, x2, x3, x4)
    ymi, ymx = min(y1, y2, y3, y4), max(y1, y2, y3, y4)
    print(max(xmx - xmi, ymx - ymi)**2)