## taeyang's template (1.0.7)
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
from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################


def solution():
    ans = []
    for combi in combinations(lst, l):
        vowel, conso = 0, 0
        for c in combi:
            if c in 'aeiou':
                vowel += 1
            else:
                conso += 1
        if vowel >= 1 and conso >= 2:
            ans.append(''.join(sorted(combi)))
    return ans


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    # n = int(input())
    l, c = map(int, input().split())
    lst = sorted(map(str, input().split()))
    
    # output
    for v in solution():
        print(v)