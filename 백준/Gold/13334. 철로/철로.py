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

def solution(n, li, d):
    max_len = 0
    pq = []
    for s, e in li:
        lim = e - d
        if s >= lim:
            heappush(pq, s)
        while pq and pq[0] < lim:
            heappop(pq)
        max_len = max(max_len, len(pq))
    return max_len

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    li = [sorted(list(map(int, input().split()))) for _ in range(n)]
    li.sort(key=lambda x: x[1])
    d = int(input())
    
    # output
    print(solution(n, li, d))