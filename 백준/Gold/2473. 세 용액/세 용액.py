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

def solution(n, li):
    res = [0] * 3
    tmp = sys.maxsize
    for i in range(n-2):
        left, right = i+1, n-1
        while left < right:
            sum_val = li[i] + li[left] + li[right]
            if abs(sum_val) < abs(tmp):
                res[0] = li[i]
                res[1] = li[left]
                res[2] = li[right]
                tmp = sum_val
            
            if sum_val < 0:
                left += 1
            elif sum_val > 0:
                right -= 1
            else:
                return res
    return res

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    
    # output
    print(*solution(n, li))