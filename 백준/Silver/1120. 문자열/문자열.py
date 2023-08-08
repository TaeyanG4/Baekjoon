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

def solution():
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    a, b = map(str, input().rstrip().split())
    min_val = INF
    for i in range(len(b) - len(a) + 1):
        cnt = 0
        for j in range(len(a)):
            if a[j] != b[i+j]:
                cnt += 1
        min_val = min(min_val, cnt)
    
    # output
    print(min_val)