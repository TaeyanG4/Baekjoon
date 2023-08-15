## taeyang's template (1.0.0)
#################################
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import time
# import pprint
from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(cmd, l, r):
    c = ord(cmd) - ord('a')
    if l == 0:
        return li[r][c]
    else:
        return li[r][c] - li[l - 1][c]

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    s = input().rstrip()
    n = int(input())
    li = [[0] * 26 for _ in range(len(s))]
    
    for i, c in enumerate(s):
        li[i][ord(c) - ord('a')] = 1
        for j in range(26):
            if i > 0:
                li[i][j] += li[i - 1][j]

    # output
    for _ in range(n):
        cmd, l, r = map(str, input().split())
        l, r, = int(l), int(r)
        print(solution(cmd, l, r))