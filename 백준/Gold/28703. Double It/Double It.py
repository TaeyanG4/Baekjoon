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
from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(n, li):
    mx = max(li)
    heapify(li)
    cur_mx = mx
    ans = cur_mx - li[0]
    while li[0] < mx:
        v = heappop(li)
        ans = min(ans, cur_mx-v)
        cur_mx = max(cur_mx, v*2)
        heappush(li, v*2)
    return min(ans, cur_mx-li[0])

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    li = list(map(int, input().split()))
    
    # output
    print(solution(n, li))