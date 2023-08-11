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

def solution(n, k, li):
    ans = -INF
    if k == 1:
        ans = max(li)
    elif k == 2:
        for i in range(1, n):
            ans = max(ans, li[i-1] + li[i])
    else:
        temp = sum(li[:k])
        ans = temp
        for i in range(n-k):
            temp = temp - li[i] + li[i+k]
            ans = max(ans, temp)
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    
    # output
    print(solution(n, k, li))