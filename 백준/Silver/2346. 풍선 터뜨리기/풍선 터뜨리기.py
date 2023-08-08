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
    dq = deque(enumerate(map(int, input().split())))
    ans = []
    while dq: 
        idx, val = dq.popleft()
        ans.append(idx+1)
        
        if val > 0:
            dq.rotate(-(val-1))
        else:
            dq.rotate(-val)
        
    # output
    print(*ans)