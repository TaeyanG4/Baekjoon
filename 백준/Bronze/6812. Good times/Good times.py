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

    t = input().rstrip()
    while len(t) != 4 :
        t = "0" + t
    h, m = t[:2], t[2:]
    
    print(int(t), "in Ottawa")
    if int(h) - 3 < 0: 
        print(int(str(int(h) - 3 + 24) + m), "in Victoria")
    else: 
        print(int(str(int(h) - 3) + m), "in Victoria")
    if int(h) - 2 < 0: 
        print(int(str(int(h) - 2 + 24) + m), "in Edmonton")
    else: 
        print(int(str(int(h) - 2) + m), "in Edmonton")
    if int(h) - 1 < 0: 
        print(int(str(int(h) - 1 + 24) + m), "in Winnipeg")
    else:
        print(int(str(int(h) - 1) + m), "in Winnipeg")
    print(int(t), "in Toronto")
    if int(h) + 1 == 24: 
        print(int(m), "in Halifax")
    else: 
        print(int(str(int(h) + 1) + m), "in Halifax")
    
    st_m = int(m) + 30
    if st_m >= 60:
        st_h = str(int(h) + 2)
        st_m -= 60
    else: 
        st_h = str(int(h) + 1)
    if st_m == 0 and st_h != 0: 
        st_m = "00"
    else:
        st_m = str(st_m)
    if int(st_h) > 23: 
        st_h = str(int(st_h) - 24)
    print(int(st_h + st_m), "in St. John's")