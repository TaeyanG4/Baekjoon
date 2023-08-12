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

def solution(n, m, k):
    temp = 0
    for i in range(1, m+1):
        t, r = map(int, input().split())
        temp += r
        if temp > k:
            return i, 1
    return [-1]
        

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m, k = map(int, input().split())
    
    # output
    print(*solution(n, m, k))