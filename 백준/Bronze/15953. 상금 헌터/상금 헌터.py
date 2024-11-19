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

    for _ in range(int(input())):
        a, b = S()
        ans = 0
        if a == 0:
            ans += 0
        elif 0 < a <= 1:
            ans += 5000000
        elif a <= 3:
            ans += 3000000
        elif a <= 6:
            ans += 2000000
        elif a <= 10:
            ans += 500000
        elif a <= 15:
            ans += 300000
        elif a <= 21:
            ans += 100000
        
        if b == 0:
            ans += 0
        elif b <= 1:
            ans += 5120000
        elif b <= 3:
            ans += 2560000
        elif b <= 7:
            ans += 1280000
        elif b <= 15:
            ans += 640000
        elif b <= 31:
            ans += 320000

        print(ans)