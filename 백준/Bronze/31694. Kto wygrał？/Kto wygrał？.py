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
    
    
    lst_a = sorted(S())
    lst_b = sorted(S())
    if sum(lst_a) > sum(lst_b):
        print("Algosia")
    elif sum(lst_a) < sum(lst_b):
        print("Bajtek")
    else:
        for i in range(10, 1, -1):
            cnt_a = lst_a.count(i)
            cnt_b = lst_b.count(i)
            if cnt_a > cnt_b:
                print("Algosia")
                break
            elif cnt_a < cnt_b:
                print("Bajtek")
                break
        else:
            print("remis")