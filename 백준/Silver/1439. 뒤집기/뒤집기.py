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
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    s = list(input().rstrip())
    zero_cnt, one_cnt = [], []
    temp = []
    cnt = 0
    while s:
        v = s.pop()
        if not temp or temp[-1] == v:
            temp.append(v)
        else:
            if temp[-1] == '0':
                zero_cnt.append(temp)
                s.append(v)
                temp = []
            else:
                one_cnt.append(temp)
                s.append(v)
                temp = []
    
    if temp[-1] == '0':
        zero_cnt.append(temp)
        s.append(v)
        temp = []
    else:
        one_cnt.append(temp)
        s.append(v)
        temp = []

    # output
    print(min(len(zero_cnt), len(one_cnt)))