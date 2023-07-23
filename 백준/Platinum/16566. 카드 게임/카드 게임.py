# import lines
#################################
import sys
# import math
# import copy
# import ast
# import re
# import time
# import json
# import time
# import pprint
# from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
from bisect import *
#################################

# https://velog.io/@sunkyuj/python-백준-16556-카드게임

def find(v):
    if v == root[v]:
        return v
    root[v] = find(root[v])
    return root[v]

def union(a, b):
    r1 = find(a)
    r2 = find(b)
    root[r1] = r2

def solution(nums, cards):
    for card in cards:
        idx = bisect_right(nums, card)
        real_idx = find(idx)
        print(nums[real_idx])
        union(real_idx, real_idx+1)

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m, k = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    cards = list(map(int, input().split()))
    root = [i for i in range(m+1)]
    
    # output
    solution(nums, cards)