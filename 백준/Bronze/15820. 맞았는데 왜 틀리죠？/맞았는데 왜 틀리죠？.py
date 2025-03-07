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

    s1, s2 = True, True
    a, b = S()
    for _ in range(a):
        aa, bb = S()
        if aa != bb:
            s1 = False
            break
    for _ in range(b):
        aa, bb = S()
        if aa != bb:
            s2 = False
            break
    
    if s1 and s2:
        print("Accepted")
    elif s1 == False:
        print("Wrong Answer")
    else:
        print("Why Wrong!!!")