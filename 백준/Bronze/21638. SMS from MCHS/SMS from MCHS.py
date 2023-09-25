## taeyang's template (1.0.7)
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
    t1, v1 = map(int, input().split())
    t2, v2 = map(int, input().split())
    if v2 >= 10 and t2 < 0:
        return 'A storm warning for tomorrow! Be careful and stay home if possible!'
    elif t1 > t2:
        return 'MCHS warns! Low temperature is expected tomorrow.'
    elif v1 < v2:
        return 'MCHS warns! Strong wind is expected tomorrow.'
    else:
        return 'No message'


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    # lst = [*map(int, input().split())]
    # n = int(input())

    # output
    print(solution())
