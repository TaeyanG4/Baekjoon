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
from collections import *
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
    n = int(input())
    li = list(map(int, input().split()))
    dq = deque()
    for idx, val in enumerate(li):
        dq.append((idx, val))
    
    ans = []
    while dq: 
        idx, val = dq.popleft()
        ans.append(idx+1)
        
        tmp = val
        if tmp > 0:
            tmp -= 1
        
        while tmp != 0 and dq:
            if tmp > 0:
                dq.append(dq.popleft())
                tmp -= 1
            else:
                dq.appendleft(dq.pop())
                tmp += 1
    
    # output
    print(*ans)