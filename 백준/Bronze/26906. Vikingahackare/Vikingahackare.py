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
from collections import *
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
    S = lambda: map(str, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    t = int(input())
    dic = defaultdict(str)
    for i in range(t):
        n, s = S()
        dic[s] = n
    ss = input().strip()
    for i in range(len(ss)//4):
        if ss[i*4:(i+1)*4] in dic:
            print(dic[ss[i*4:(i+1)*4]], end='')
        else:
            print('?', end='')