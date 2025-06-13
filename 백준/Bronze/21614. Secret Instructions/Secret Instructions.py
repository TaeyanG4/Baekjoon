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
# getcontext().prec = 20
#################################


def solution():
    pass


if __name__ == "__main__":
    # input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    save = ''
    while True:
        n = input().rstrip()
        if n == '99999':
            break
        front1, front2 = int(n[0]), int(n[1])
        sm = front1 + front2
        if sm == 0:
            print(save, n[2:])
        elif sm % 2 == 1:
            save = 'left'
            print(save, n[2:])
        elif sm % 2 == 0:
            save = 'right'
            print(save, n[2:])
    