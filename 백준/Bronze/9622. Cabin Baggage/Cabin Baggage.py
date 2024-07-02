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
    S = lambda: map(float, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    total = 0
    for _ in range(int(input())):
        flag = False
        l, w, d, exd = S()
        if (l <= 56 and w <= 45 and d <= 25) or (l + w + d <= 125):
            if exd <= 7:
                total += 1
                print(1)
            else:
                print(0)
        else:
            print(0) 
    print(total)
    
    