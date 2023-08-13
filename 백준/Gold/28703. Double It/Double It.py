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

def solution(n):
    mx = 0
    pq = []
    for v in map(int, input().split()):
        mx = max(mx, v)
        heappush(pq, v)
    
    cur_mx = mx
    ans = cur_mx - pq[0]
    while pq[0] < mx:
        v = heappop(pq)
        ans = min(ans, cur_mx-v)
        cur_mx = max(cur_mx, v*2)
        heappush(pq, v*2)
    return min(ans, cur_mx-pq[0])

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    
    # output
    print(solution(n))