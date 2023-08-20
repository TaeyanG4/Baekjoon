## taeyang's template (1.0.1)
# https://claude-u.tistory.com/449
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

def solution(n, k):
    
    s, e = 1, k
    while s < e:
        
        mid = (s+e)//2
        cnt = 0
        for i in range(1, n+1):
            cnt += min(mid//i, n)
            
        if cnt < k:
            s = mid + 1
        else:
            e = mid
            
    return s

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    k = int(input())
    
    # for test
    # mat = []
    # li = []
    # for i in range(1, n+1):
    #     temp = []
    #     for j in range(1, n+1):
    #         temp.append(i*j)
    #         li.append(i*j)
    #     mat.append(temp)
    # pprint.pprint(mat)
    
    # output
    print(solution(n, k))