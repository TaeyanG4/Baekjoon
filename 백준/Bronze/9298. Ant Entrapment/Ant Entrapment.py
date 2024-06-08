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
    S = lambda: map(float, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(int(input())):
        xmi, xmx, ymi, ymx = INF, -INF, INF, -INF
        for _ in range(int(input())):
            x, y = S()
            xmi, xmx = min(xmi, x), max(xmx, x)
            ymi, ymx = min(ymi, y), max(ymx, y)
        print(f'Case {i+1}: Area {(xmx-xmi)*(ymx-ymi)}, Perimeter {2*(xmx-xmi+ymx-ymi)}')