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

    while True:
        k = int(input())
        if k == 0:
            break
        x, y = S()
        for _ in range(k):
            xx, yy = S()
            if xx == x or yy == y:
                print("divisa")
            elif xx > x and yy > y:
                print("NE")
            elif xx < x and yy > y:
                print("NO")
            elif xx < x and yy < y:
                print("SO")
            else:
                print("SE")