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

    # input
    # n = int(input())
    # n, m = map(int, input().split())
    # lst = [*map(int, input().split())]
    
    lst = [int(input()) for _ in range(8)]
    sorted_lst = sorted(lst)
    top_5 = sorted_lst[-5:]
    rank = [lst.index(i) + 1 for i in top_5]
    print(sum(top_5))
    print(*sorted(rank))