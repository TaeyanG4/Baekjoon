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

    for i in range(100, 1000):
        for j in range(100, 1000):
            if i % 111 == 0 and j % 111 == 0:
                continue
            if (j % 100) == 0:
                continue
            if str(i)[2] == str(j)[0]:
                if i / j == (i // 10) / (j % 100):
                    print(f'{i} / {j} = {(i // 10)} / {(j % 100)}')