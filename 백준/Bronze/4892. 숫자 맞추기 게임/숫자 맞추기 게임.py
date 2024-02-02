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

    cnt = 0
    while True:
        cnt += 1
        n = int(input())
        if n == 0:
            break
        
        n1 = 3 * n
        if n1 % 2 == 0:
            print(f"{cnt}. even", end=" ")
            n2 = n1 // 2
        else:
            print(f"{cnt}. odd", end=" ")
            n2 = (n1 + 1) // 2
        
        n3 = 3 * n2
        n4 = n3 // 9
        print(n4)