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
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(int(input())):
        s = input()
        for c in s:
            if c == 'a':
                print('e', end='')
            elif c == 'e':
                print('i', end='')
            elif c == 'i':
                print('o', end='')
            elif c == 'o':
                print('u', end='')
            elif c == 'u':
                print('y', end='')
            elif c == 'y':
                print('a', end='')
            elif c == 'A':
                print('E', end='')
            elif c == 'E':
                print('I', end='')
            elif c == 'I':
                print('O', end='')
            elif c == 'O':
                print('U', end='')
            elif c == 'U':
                print('Y', end='')
            elif c == 'Y':
                print('A', end='')
            else:
                print(c, end='')
    