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
    cnt = 0
    for i in dic[cmd]:
        if int(l) <= i <= int(r):
            cnt += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    s = input().rstrip()
    n = int(input())
    dic = defaultdict(list)
    
    for i, c in enumerate(s):
        dic[c].append(i)
    
    # output
    for _ in range(n):
        cmd, l, r = map(str, input().split())
        print(solution(cmd, l, r))