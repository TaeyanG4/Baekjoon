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
    S = lambda: map(str, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    s = input().strip()
    n = int(input())
    ans = ('No Jam', 0)
    for _ in range(n):
        w, g = S()
        w_tmp, g = w, int(g)
        tmp, s_cnt = 0, 0
        for c in s:
            while w_tmp:
                if c == w_tmp[0]:
                    w_tmp = w_tmp[1:]
                    s_cnt += 1
                    break
                else:
                    tmp += 1
                    w_tmp = w_tmp[1:]
        if tmp+len(w_tmp) and s_cnt == len(s):
            if ans[1] < g/(tmp+len(w_tmp)):
                ans = (w, g/(tmp+len(w_tmp)))
    print(ans[0])