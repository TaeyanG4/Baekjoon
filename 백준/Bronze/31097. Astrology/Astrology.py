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
# getcontext().prec = 20
#################################

def solution():
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(str, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    yy, mm, dd = input().strip().split('-')
    yy, mm, dd = int(yy), int(mm), int(dd)
    if mm == 3 and dd >= 21:
        print("Aries")
    elif mm == 4 and dd <= 19:
        print("Aries")
    elif mm == 4 and dd >= 20:
        print("Taurus")
    elif mm == 5 and dd <= 20:
        print("Taurus")
    elif mm == 5 and dd >= 21:
        print("Gemini")
    elif mm == 6 and dd <= 20:
        print("Gemini")
    elif mm == 6 and dd >= 21:
        print("Cancer")
    elif mm == 7 and dd <= 22:
        print("Cancer")
    elif mm == 7 and dd >= 23:
        print("Leo")
    elif mm == 8 and dd <= 22:
        print("Leo")
    elif mm == 8 and dd >= 23:
        print("Virgo")
    elif mm == 9 and dd <= 22:
        print("Virgo")
    elif mm == 9 and dd >= 23:
        print("Libra")
    elif mm == 10 and dd <= 22:
        print("Libra")
    elif mm == 10 and dd >= 23:
        print("Scorpio")
    elif mm == 11 and dd <= 22:
        print("Scorpio")
    elif mm == 11 and dd >= 23:
        print("Sagittarius")
    elif mm == 12 and dd <= 21:
        print("Sagittarius")
    elif mm == 12 and dd >= 22:
        print("Capricorn")
    elif mm == 1 and dd <= 19:
        print("Capricorn")
    elif mm == 1 and dd >= 20:
        print("Aquarius")
    elif mm == 2 and dd <= 18:
        print("Aquarius")
    elif mm == 2 and dd >= 19:
        print("Pisces")
    elif mm == 3 and dd <= 20:
        print("Pisces")