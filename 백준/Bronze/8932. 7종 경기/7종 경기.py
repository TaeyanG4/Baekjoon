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
    
    data = {
        "100미터 허들": {"A": 9.23076, "B": 26.7, "C": 1.835, "unit": "sec", "type": "트랙"},
        "높이뛰기": {"A": 1.84523, "B": 75, "C": 1.348, "unit": "cm", "type": "필드"},
        "포환던지기": {"A": 56.0211, "B": 1.5, "C": 1.05, "unit": "m", "type": "필드"},
        "200미터 달리기": {"A": 4.99087, "B": 42.5, "C": 1.81, "unit": "sec", "type": "트랙"},
        "멀리뛰기": {"A": 0.188807, "B": 210, "C": 1.41, "unit": "cm", "type": "필드"},
        "창던지기": {"A": 15.9803, "B": 3.8, "C": 1.04, "unit": "m", "type": "필드"},
        "800미터 달리기": {"A": 0.11193, "B": 254, "C": 1.88, "unit": "sec", "type": "트랙"}
    }

    for _ in range(int(input())):
        score = 0
        lst = list(map(int, input().split()))
        for i, v in enumerate(data.keys()):
            if data[v]["type"] == "트랙":
                score += int(data[v]["A"] * (data[v]["B"] - lst[i])**data[v]["C"])
            else:
                score += int(data[v]["A"] * (lst[i] - data[v]["B"])**data[v]["C"])
        print(score)