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

def solution(n):
    stack = []
    q = deque(map(int, input().split()))
    cnt = 1
    
    while q:
        if q and q[0] == cnt:
            q.popleft()
            cnt += 1
        else:
            stack.append(q.popleft())
        while stack and stack[-1] == cnt:
            stack.pop()
            cnt += 1
    
    return 'Nice' if not stack else 'Sad'

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    
    # output
    print(solution(n))