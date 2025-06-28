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
# getcontext().prec = 20
#################################


def solution():
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(str, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    for i in range(int(input())):
        t1, t2, k = S()
        t1, t2 = datetime.strptime(t1, '%H:%M:%S'), datetime.strptime(t2, '%H:%M:%S')
        k = timedelta(minutes=int(k)).total_seconds()
        if t1 >= t2:
            t2 += timedelta(days=1)
        t = t2 - t1
        if  k <= t.total_seconds():
            print('Perfect')
        elif t.total_seconds() < k <= t.total_seconds()+3600:
            print('Test')
        else:
            print('Fail')