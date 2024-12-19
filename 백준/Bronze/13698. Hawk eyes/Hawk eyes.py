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

    dic = {
        'A': [0, 1],
        'B': [0, 2],
        'C': [0, 3],
        'D': [1, 2],
        'E': [1, 3],
        'F': [2, 3], 
    }
    
    lst = ['small', '', '', 'big']
    for c in input().strip():
        c1, c2 = dic[c]
        lst[c1], lst[c2] = lst[c2], lst[c1]
    print(lst.index('small')+1)
    print(lst.index('big')+1)