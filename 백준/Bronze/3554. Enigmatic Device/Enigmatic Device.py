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
    MOD = 2010
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # input
    n = int(input())
    ai = [*map(int, input().split())]
    m = int(input())
    
    for i in range(m):
        kj, lj, rj = S()
        func1 = lambda x: x**2 % MOD
        if kj == 1:
            for j in range(lj-1, rj):
                ai[j] = func1(ai[j])
        else:
            print(sum(ai[lj-1:rj]))