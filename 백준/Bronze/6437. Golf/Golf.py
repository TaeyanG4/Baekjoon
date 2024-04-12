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

    cnt = 1
    while True:
        p, s = S()
        if p == s == 0:
            break
        print(f"Hole #{cnt}")
        tmp = p - s
        if s == 1:
            print("Hole-in-one.")
        elif tmp == 3:
            print("Double Eagle.")
        elif tmp == 2:
            print("Eagle.")
        elif tmp == 1:
            print("Birdie.")
        elif tmp == 0:
            print("Par.")
        elif tmp == -1:
            print("Bogey.")
        else:
            print("Double Bogey.")
        print()
        cnt +=1