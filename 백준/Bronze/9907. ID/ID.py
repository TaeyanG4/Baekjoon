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

    n = input().strip()
    tmp = ((int(n[0])*2)+(int(n[1])*7)+(int(n[2])*6)+(int(n[3])*5)+(int(n[4])*4)+(int(n[5])*3)+(int(n[6])*2)) % 11
    if tmp == 0:
        print('J')
    elif tmp == 1:
        print('A')
    elif tmp == 2:
        print('B')
    elif tmp == 3:
        print('C')
    elif tmp == 4:
        print('D')
    elif tmp == 5:
        print('E')
    elif tmp == 6:
        print('F')
    elif tmp == 7:
        print('G')
    elif tmp == 8:
        print('H')
    elif tmp == 9:
        print('I')
    elif tmp == 10:
        print('Z')