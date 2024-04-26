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

    cnt = 1
    while True:
        a, b, c = S()
        if a == b == c == 0:
            break
        if c == -1:
            print(f"Triangle #{cnt}")
            print(f"c = {math.sqrt(a**2 + b**2):.3f}")
        elif a == -1:
            if b < c:
                print(f"Triangle #{cnt}")
                print(f"a = {math.sqrt(c**2 - b**2):.3f}")
            else:
                print(f"Triangle #{cnt}")
                print("Impossible.")
        elif b == -1:
            if a < c:
                print(f"Triangle #{cnt}")
                print(f"b = {math.sqrt(c**2 - a**2):.3f}")
            else:
                print(f"Triangle #{cnt}")
                print("Impossible.")
        print()
        cnt += 1