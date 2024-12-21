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

    while True:
        
        n = int(input())
        if n == 0:
            break
        if n % 4 == 0 and n >= 1896:
            if n >= 2024:
                print(f"{n} No city yet chosen")
            elif 1914 <= n <= 1918 or 1939 <= n <= 1945:
                print(f"{n} Games cancelled")
            else:
                print(f"{n} Summer Olympics")
        else:
            print(f"{n} No summer games")