# import lines
#################################
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
# from datetime import datetime
# from bisect import *
#################################

def solution(n):
    s = str(n)
    ans = len(s)+1
    for c in s:
        if c == '0':
            ans += 4
        elif c == '1':
            ans += 2
        else:
            ans += 3
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while True:
        # input
        n = int(input())
        
        if n == 0:
            break
        
        # output
        print(solution(n))