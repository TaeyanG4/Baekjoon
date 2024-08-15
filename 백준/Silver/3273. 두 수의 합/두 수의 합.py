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

def solution(n, li, x):
    left = 0
    right = n - 1
    ans = 0
    while left < right:
        if li[left] + li[right] == x:
            ans += 1
            left += 1
        elif li[left] + li[right] < x:
            left += 1
        else:
            right -= 1
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    li = [*map(int, input().split())]
    li.sort()
    x = int(input())
    
    # output
    print(solution(n, li, x))