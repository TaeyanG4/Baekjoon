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

    for _ in range(int(input())):
        s = input().strip()
        sm = 0
        for c in s:
            sm += int(c)
        
        n = int(s[10:]) * 10
        ans = sm + n
        if ans > 9999:
            print(str(ans)[1:])
        elif ans < 1000:
            print(ans + 1000)
        else:
            print(ans)
        