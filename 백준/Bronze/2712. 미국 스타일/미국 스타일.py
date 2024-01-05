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
        n, s = map(str, input().split())
        n = float(n)
        if s == 'kg':
            print(f'{n*2.2046:.4f} lb')
        elif s == 'lb':
            print(f'{n*0.4536:.4f} kg')
        elif s == 'l':
            print(f'{n*0.2642:.4f} g')
        elif s == 'g':
            print(f'{n*3.7854:.4f} l')