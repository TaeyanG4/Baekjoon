## taeyang's template (1.0.7)
#################################
## my import lines
import sys
import math
# import copy
# import ast
import re
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


if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    # n, m = map(int, input().split())
    # lst = [*map(int, input().split())]
    
    n = int(input())
    str_sep = [*map(str, input().split())]
    m = int(input())
    num_sep = [*map(str, input().split())]
    k = int(input())
    merge_lst = [*map(str, input().split())]
    str_len = int(input())
    s = input().rstrip()
    
    all_sep = []
    all_sep.extend(str_sep)
    all_sep.extend(num_sep)
    all_sep.append(' ')
    set_sep = set(all_sep)
    merge_sep = set(merge_lst)
    new_sep = set_sep - merge_sep
    
    for sep in new_sep:
        s = s.replace(sep, ' ')
    
    for c in s.split():
        print(c)