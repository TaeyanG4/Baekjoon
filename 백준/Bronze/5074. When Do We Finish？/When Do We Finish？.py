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
    S = lambda: map(str, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while True:
        # input
        a, b = S()
        if a == '00:00' and b == '00:00':
            break
        time1_h, time1_m = map(int, a.split(':'))
        time2_h, time2_m = map(int, b.split(':'))
        
        delta1 = timedelta(hours=time1_h, minutes=time1_m)
        delta2 = timedelta(hours=time2_h, minutes=time2_m)
        ans = delta1 + delta2
        # output
        if ans.days:
            print(f'{ans.seconds//3600:02d}:{ans.seconds%3600//60:02d} +{ans.days}')
        else:
            print(f'{ans.seconds//3600:02d}:{ans.seconds%3600//60:02d}')