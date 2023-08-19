## taeyang's template (1.0.1)
# https://my-coding-notes.tistory.com/119
#################################
## my import lines
import sys
# import math
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
    s, e = 1, (li[-1]-li[0]) // (c-1) + 1
    while s < e:
        m = (s + e) // 2
        cnt, v  = 1, li[0]
        for i in li:
            if i - v >= m:
                cnt, v =  cnt+1, i
        
        if cnt >= c:
            ans = m
            s = m+1
        else:
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