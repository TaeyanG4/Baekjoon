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
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    # n = int(input())
    t1, e1, f1 = map(int, input().split())
    t2, e2, f2 = map(int, input().split())
    sm1 = t1*3 + e1*20 + f1*120
    sm2 = t2*3 + e2*20 + f2*120

    
    # output
    print('Max' if sm1 > sm2 else 'Mel' if sm1 < sm2 else 'Draw')