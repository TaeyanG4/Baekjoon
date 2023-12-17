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
    board = [list(input().rstrip()) for _ in range(8)]
    b, w = 0, 0
    for line in board:
        for i in line:
            if i == 'P':
                w += 1
            elif i == 'p':
                b += 1
            elif i == 'N':
                w += 3
            elif i == 'n':
                b += 3
            elif i == 'B':
                w += 3
            elif i == 'b':
                b += 3
            elif i == 'R':
                w += 5
            elif i == 'r':
                b += 5
            elif i == 'Q':
                w += 9
            elif i == 'q':
                b += 9
        
    # output
    print(w-b)
