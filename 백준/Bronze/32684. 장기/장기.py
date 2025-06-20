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
    
    lst_1 = [*S()]
    lst_2 = [*S()]
    sm_1 = lst_1[0]*13 + lst_1[1]*7 + lst_1[2]*5 + lst_1[3]*3 + lst_1[4]*3 + lst_1[5]*2
    sm_2 = lst_2[0]*13 + lst_2[1]*7 + lst_2[2]*5 + lst_2[3]*3 + lst_2[4]*3 + lst_2[5]*2 + 1.5
    if sm_1 > sm_2:
        print("cocjr0208")
    else:
        print("ekwoo")