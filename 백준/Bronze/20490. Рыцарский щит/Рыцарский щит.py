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
from decimal import *
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
    
    a1, b1, c1 = S()
    a2, b2, c2 = S()
    mx1 = max(a1, b1, c1)
    mx2 = max(a2, b2, c2)
    ans = a1 + b1 + c1 + a2 + b2 + c2 - mx1 - mx2 + abs(mx1 - mx2)
    print(ans)
