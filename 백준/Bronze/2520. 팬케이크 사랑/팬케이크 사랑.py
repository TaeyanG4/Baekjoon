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

    for _ in range(int(input())):
        tmp = input()
        cm, y, ssu, ssa, f = S()
        b, gs, gc, w = S()
        cm, y, ssu, f = cm / 8, y / 8, ssu / 4, f / 9
        dough = int(min(cm, y, ssu, ssa, f) * 16)
        gs, gc, w = gs // 30, gc // 25, w // 10
        toppings = b + gs + gc + w
        if dough >= toppings:
            print(toppings)
        else:
            print(dough)