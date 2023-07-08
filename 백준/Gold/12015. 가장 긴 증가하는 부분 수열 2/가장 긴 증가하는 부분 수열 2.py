# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
from bisect import *
#################################

def solution(n, a):
    li = [-1*sys.maxsize]
    li_idx = [(-1*sys.maxsize, 0)]
    a = a[::-1]
    
    while a:
        v = a.pop()
        if v > li[-1]:
            li_idx.append((v, len(li)))
            li.append(v)
        else:
            idx = bisect_left(li, v)
            li[idx] = v
            li_idx.append((v, idx))
    
    return len(li)-1

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n = int(input())
    a = list(map(int, input().split()))
    
    # output
    print(solution(n, a))
    