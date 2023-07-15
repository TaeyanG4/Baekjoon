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

# https://yiyj1030.tistory.com/490

def get_psum(x):
    ans = 0
    bin_n = bin(x)[2:]
    length = len(bin_n)
    for i in range(length):
        if bin_n[i] == '1':
            val = length - i - 1
            ans += psum[val]
            ans += x - 2**val + 1
            x = x - 2**val
    return ans

def solution(a, b):
    return get_psum(b) - get_psum(a-1)

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    a, b = map(int, input().split())
    psum = [0] * 60
    for i in range(1, 60):
        psum[i] = 2**(i-1) + 2 * psum[i-1]
    
    # output
    print(solution(a, b))