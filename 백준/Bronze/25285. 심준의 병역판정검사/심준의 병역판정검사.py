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

def grade_by_height_weight(h_cm, w_kg):
    bmi = w_kg / ((h_cm / 100) ** 2)

    if h_cm < 140.1:
        return 6
    elif h_cm < 146:
        return 5
    elif h_cm < 159:
        return 4
    elif h_cm < 161:
        # 159 이상 161 미만
        if 16.0 <= bmi < 35.0:
            return 3
        else:  # bmi < 16.0 or bmi >= 35.0
            return 4
    elif h_cm < 204:
        # 161 이상 204 미만
        if 20.0 <= bmi < 25.0:
            return 1
        elif (18.5 <= bmi < 20.0) or (25.0 <= bmi < 30.0):
            return 2
        elif (16.0 <= bmi < 18.5) or (30.0 <= bmi < 35.0):
            return 3
        else:  # bmi < 16.0 or bmi >= 35.0
            return 4
    else:
        # 204 이상
        return 4


def solution():
    t = int(input().strip())
    for _ in range(t):
        h_str, w_str = input().split()
        h = float(h_str)  # cm
        w = float(w_str)  # kg
        print(grade_by_height_weight(h, w))


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(str, input().split())
    INF = float('inf')
    solution()