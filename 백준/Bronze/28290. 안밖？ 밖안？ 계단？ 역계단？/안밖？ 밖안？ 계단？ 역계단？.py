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

    # input
    s = input().rstrip()

    
    # output
    if s == "fdsajkl;" or s == "jkl;fdsa":
        print("in-out")
    elif s == "asdf;lkj" or s == ";lkjasdf":
        print("out-in")
    elif s == "asdfjkl;":
        print("stairs")
    elif s == ";lkjfdsa":
        print("reverse")
    else:
        print("molu")