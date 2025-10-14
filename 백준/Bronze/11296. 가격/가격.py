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

    
# 점의 색깔	할인율%
# 빨강색	45
# 초록색	30
# 파란색	20
# 노란색	15
# 주황색	10
# 흰색	5
        
    for i in range(int(input())):
        price, color, coupon, pay = S()
        price = float(price)
        if color == "R":
            price *= 0.55
        elif color == "G":
            price *= 0.70
        elif color == "B":
            price *= 0.80
        elif color == "Y":
            price *= 0.85
        elif color == "O":
            price *= 0.90
        elif color == "W":
            price *= 0.95
    
        if coupon == "C":
            price *= 0.95
        if pay == "C":
            price = math.floor(price * 10 + 0.4) / 10
        
        print(f'${price:.2f}')
        
            