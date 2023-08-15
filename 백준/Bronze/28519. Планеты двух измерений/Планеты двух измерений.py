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

def solution(n, m):
    mi = min(n, m)
    mx = max(n, m)
    if mi == mx:
        return n + m
    else:
        return (mi * 2) + 1

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    
    # output
    print(solution(n, m))