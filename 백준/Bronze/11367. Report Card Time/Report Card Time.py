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
    S = lambda: map(str, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for _ in range(int(input())):
        name, score = input().split()
        score = int(score)
        if score >= 97:
            print(name, "A+")
        elif score >= 90:
            print(name, "A")
        elif score >= 87:
            print(name, "B+")
        elif score >= 80:
            print(name, "B")
        elif score >= 77:
            print(name, "C+")
        elif score >= 70:
            print(name, "C")
        elif score >= 67:
            print(name, "D+")
        elif score >= 60:
            print(name, "D")
        else:
            print(name, "F")
