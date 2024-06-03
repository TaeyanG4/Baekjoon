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
from itertools import *
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
    
    lst1, lst2 = [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]
    for i in range(int(input())):
        set1 = set()
        n = int(input())
        print(f'Case {i+1}:')
        if n < 2 or n > 12:
            continue
        for a, b in product(lst1, lst2):
            if a + b == n:
                if a > b:
                    a, b = b, a
                set1.add((a, b))
        for a, b in sorted(set1):
            print(f'({a},{b})')