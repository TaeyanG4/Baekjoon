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

def solution():
    s, e = 0, len(li)-1
    min_val, save_p = abs(li[s]+li[e]), (s, e)
    
    while s < e:
        
        tmp = li[s]+li[e]
        
        if abs(tmp) < min_val:
            if tmp == 0:
                return s, e
            save_p = s, e
            min_val = abs(tmp)
            
        if tmp > 0:
            e -= 1
        else:
            s += 1
            
    return save_p

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n = map(int, input().split())
    li = list(map(int, input().split()))
    
    # output
    s, e = solution()
    print(li[s], li[e])
