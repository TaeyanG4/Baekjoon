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

    # input
    t1 = input().strip()
    t2 = input().strip()
    t1 = datetime.strptime(t1, '%H:%M:%S')
    t2 = datetime.strptime(t2, '%H:%M:%S')
    if t1 > t2:
        t2 += timedelta(days=1)
        
    # output
    if t1 == t2:
        print('24:00:00')
    else:
        delta = t2 - t1
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")