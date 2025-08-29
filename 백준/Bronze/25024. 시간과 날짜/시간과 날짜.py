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
# getcontext().prec = 20
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
    
    for i in range(int(input())):
        x, y = S()
        if x <= 23 and y <= 59:
            print("Yes", end=" ")
        else:
            print("No", end=" ")
        if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
            if 1 <= y <= 31:
                print("Yes")
            else:
                print("No")
        elif x == 4 or x == 6 or x == 9 or x == 11:
            if 1 <= y <= 30:
                print("Yes")
            else:
                print("No")
        elif x == 2:
            if 1 <= y <= 29:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
