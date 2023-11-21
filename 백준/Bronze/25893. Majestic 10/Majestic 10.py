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
    n = int(input())
    
    # output
    for i in range(n):
        
        lst = [*map(int, input().split())]
        cnt = 0
        
        for v in lst:
            if v >= 10:
                cnt += 1
        
        if cnt == 3:
            print(*lst)
            print("triple-double")
        elif cnt == 2:
            print(*lst)
            print("double-double")
        elif cnt == 1:
            print(*lst)
            print("double")
        elif cnt == 0:
            print(*lst)
            print("zilch")
        print()