# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################

def solution(n, s, seq):
    l, r = 0, 0
    sum_val = 0
    min_len = sys.maxsize
    while True:
        if sum_val >= s:
            min_len = min(min_len, r-l)
            sum_val -= seq[l]
            l += 1
        elif r == n:
            break
        else:
            sum_val += seq[r]
            r += 1
    
    if min_len == sys.maxsize:
        return 0
    else:
        return min_len
            
if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n, s = map(int, input().split())
    seq = list(map(int, input().split()))
    
    # output
    print(solution(n, s, seq))

