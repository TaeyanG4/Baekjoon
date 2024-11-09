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
from datetime import *
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

    hh, mm, ss = map(int, input().split())
    delta = timedelta(hours=hh, minutes=mm, seconds=ss)
    for _ in range(int(input())):
        lst = [*S()]
        q = lst[0]
        if q == 1:
            t = lst[1]
            delta += timedelta(seconds=t)
        elif q == 2:
            t = lst[1]
            delta -= timedelta(seconds=t)
        else:
            total_sec = delta.total_seconds() % 86400
            print(int(total_sec // 3600), int(total_sec % 3600 // 60), int(total_sec % 60))