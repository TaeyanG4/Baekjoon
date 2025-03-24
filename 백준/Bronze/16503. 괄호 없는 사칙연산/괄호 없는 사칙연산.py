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
    S = lambda: map(str, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    a, op1, b, op2, c = S()
    tmp1 = int(eval(f'{a}{op1}{b}'))
    tmp2 = int(eval(f'{b}{op2}{c}'))
    ans1 = int(eval(f'{tmp1}{op2}{c}'))
    ans2 = int(eval(f'{a}{op1}{tmp2}'))
    print(min(ans1, ans2))
    print(max(ans1, ans2))