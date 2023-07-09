# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def solution(n, m, li):
    dq = deque([i for i in range(1, n+1)])
    ans = 0
    
    for i in li:
        idx = dq.index(i)
        if idx <= len(dq) // 2:
            while dq[0] != i:
                dq.append(dq.popleft())
                ans += 1
        else:
            while dq[0] != i:
                dq.appendleft(dq.pop())
                ans += 1
        dq.popleft()
    
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    
    # output
    print(solution(n, m, li))
