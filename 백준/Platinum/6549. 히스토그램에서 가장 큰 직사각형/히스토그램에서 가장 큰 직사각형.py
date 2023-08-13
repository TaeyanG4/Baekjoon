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

def solution(n, li):
    stack = []
    ans = 0
    for i in range(n):
        while stack and li[stack[-1]] > li[i]:
            height = li[stack.pop()]
            width = i
            if stack:
                width = i - stack[-1] - 1
            ans = max(ans, height * width)
        stack.append(i)
    
    while stack:
        height = li[stack.pop()]
        width = n
        if stack:
            width = n - stack[-1] - 1
        ans = max(ans, height * width)
    
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    

    
    
    while True:
        
        # input
        n, *li = map(int, input().split())
        if n == 0:
            break
        
        # output
        print(solution(n, li))