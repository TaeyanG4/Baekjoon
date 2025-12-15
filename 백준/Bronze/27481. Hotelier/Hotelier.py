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

    n = int(input())
    s = input().rstrip()
    room = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for c in s:
        if c == 'L':
            for i in range(10):
                if room[i] == 0:
                    room[i] = 1
                    break
        elif c == 'R':
            for i in range(9, -1, -1):
                if room[i] == 0:
                    room[i] = 1
                    break
        else:
            room[int(c)] = 0
    print(''.join(map(str, room)))