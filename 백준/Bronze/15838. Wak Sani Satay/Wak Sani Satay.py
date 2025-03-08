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

    cnt = 0
    while True:
        n = int(input())
        
        cnt += 1
        if n == 0:
            break
        ans = 0
        for _ in range(n):
            a, b, c, d = S()
            ans += ((a*0.8)+(b*1.0)+(c*1.2)+(d*0.8)) - (((a*7.5)+(b*24)+(c*32))/85+(d*0.2)) - (a+b+c)/85*8
        print(f"Case #{cnt}: RM{ans:.2f}")