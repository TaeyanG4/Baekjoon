## taeyang's template (1.0.1)
# https://my-coding-notes.tistory.com/119
#################################
## my import lines
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
# from datetime import *
# from bisect import *
#################################

def solution(n, c, li):
    
    if c == 2:
        return li[-1] - li[0]
    
    ans = -INF
    s, e = 1, li[-1]-li[0]
    while s < e:
        m = (s + e) // 2
        temp = li[0]
        cnt = 1
        for i in range(n):
            if li[i] - temp >= m:
                temp = li[i]
                cnt += 1
        
        if cnt >= c:
            s = m + 1
            ans = m
        elif cnt < c:
            e = m
    
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, c = map(int, input().split())
    li = sorted(int(input()) for _ in range(n))
    
    # output
    print(solution(n, c, li))