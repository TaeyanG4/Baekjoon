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

    n, d = S()
    for _ in range(n):
        for c in input().strip():
            if d == 1:
                if c == 'd':
                    print('q', end='')
                elif c == 'q':
                    print('d', end='')
                elif c == 'b':
                    print('p', end='')
                elif c == 'p':
                    print('b', end='')
            elif d == 2:
                if c == 'b':
                    print('d', end='')
                elif c == 'd':
                    print('b', end='')
                elif c == 'q':
                    print('p', end='')
                elif c == 'p':
                    print('q', end='')
        print()
        