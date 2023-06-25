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
from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def solution(k, n, v):
    pq = []
    for i in v:
        heappush(pq, i)
    
    for _ in range(n):
        num = heappop(pq)
        for i in range(k):
            tmp = num * v[i]
            heappush(pq, tmp)
            
            # 중복 소수 제거
            if num % v[i] == 0:
                break
    
    return num

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    k, n = map(int, input().split())
    v = list(map(int, input().split()))
    
    # output
    print(solution(k, n, v))

