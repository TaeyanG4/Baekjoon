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
from collections import *
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
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    win, win_p = S()
    f3_1, f3_1_p = S()
    f3_2, f3_2_p = S()
    b3_1, b3_1_p = S()
    b3_2, b3_2_p = S()
    b2_1, b2_1_p = S()
    while True:
        n = input().strip()
        if n == '-1':
            break
        ans = 0
        if n == win:
            ans += int(win_p)
        if n[:3] == f3_1:
            ans += int(f3_1_p)
        if n[:3] == f3_2:
            ans += int(f3_2_p)
        if n[3:] == b3_1:
            ans += int(b3_1_p)
        if n[3:] == b3_2:
            ans += int(b3_2_p)
        if n[4:] == b2_1:
            ans += int(b2_1_p)
        print(ans)