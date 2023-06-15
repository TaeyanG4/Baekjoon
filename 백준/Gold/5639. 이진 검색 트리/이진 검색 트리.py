# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################

def solution(s, e):
    if s > e:
        return
    mid = e+1
    for i in range(s+1, e+1):
        if nums[s] < nums[i]:
            mid = i
            break
    
    solution(s+1, mid-1)
    solution(mid, e)
    print(nums[s])
        
if __name__ == '__main__':
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)
    
    # input
    nums = []
    while True:
        try:
            nums.append(int(input()))
        except:
            break
        
    # output
    solution(0, len(nums)-1)
