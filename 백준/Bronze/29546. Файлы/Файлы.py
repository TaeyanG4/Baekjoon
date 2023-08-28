## taeyang's template (1.0.1)
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
# from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
#################################

def solution():
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    li = [input().rstrip() for _ in range(n)]
    
    # output
    ans = []
    m = int(input())
    for _ in range(m):
        s, e = map(int, input().split())
        s -= 1
        e -= 1
        ans.extend(li[s:e+1])
        
    for v in ans:
        print(v)