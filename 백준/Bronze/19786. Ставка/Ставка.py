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
#################################


def solution():
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    for _ in range(int(input())):
        a, c = S()
        r, g, b = S()
        rplus = a*((r+1)**2 + g**2 + b**2) + c*min((r+1), g, b)
        gplus = a*(r**2 + (g+1)**2 + b**2) + c*min(r, (g+1), b)
        bplus = a*(r**2 + g**2 + (b+1)**2) + c*min(r, g, (b+1))
        if rplus > gplus:
            if rplus > bplus:
                print("RED")
            else:
                print("BLUE")
        else:
            if gplus > bplus:
                print("GREEN")
            else:
                print("BLUE")