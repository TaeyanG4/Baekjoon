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
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    s1, s2, s3 = S()
    n = int(input())
    ans = -INF
    for i in range(n):
        a1, b2, c3 = S()
        a4, b5, c6 = S()
        a7, b8, c9 = S()
        
        ss1, ss2, ss3 = s1*a1, s2*b2, s3*c3
        ss4, ss5, ss6 = s1*a4, s2*b5, s3*c6
        ss7, ss8, ss9 = s1*a7, s2*b8, s3*c9

        ans = max(ans, ss1+ss2+ss3+ss4+ss5+ss6+ss7+ss8+ss9)
    print(ans)