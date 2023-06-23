# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
from bisect import *
#################################

def solution(t, n, li_a, m, li_b):
    a_sum, b_sum = [], []
    ans = 0
    for i in range(n):
        s = li_a[i]
        a_sum.append(s)
        for j in range(i+1, n):
            s += li_a[j]
            a_sum.append(s)
            
    for i in range(m):
        s = li_b[i]
        b_sum.append(s)
        for j in range(i+1, m):
            s += li_b[j]
            b_sum.append(s)
            
    a_sum.sort(); b_sum.sort()
    
    for i in range(len(a_sum)):
        l = bisect_left(b_sum, t-a_sum[i])
        r = bisect_right(b_sum, t-a_sum[i])
        ans += r-l
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    t = int(input())
    n = int(input())
    li_a = list(map(int, input().split()))
    m = int(input())
    li_b = list(map(int, input().split()))
    
    # output
    print(solution(t, n, li_a, m, li_b))

# 모범답안
# T = int(input())
# n = int(input())
# A = list(map(int, input().split()))
# m = int(input())
# B = list(map(int, input().split()))

# ans = 0
# A_dict = defaultdict(int)

# for i in range(n):
#     for j in range(i, n):
#         A_dict[sum(A[i:j+1])] += 1

# for i in range(m):
#     for j in range(i, m):
#         ans += A_dict[T - sum(B[i:j+1])]

# print(ans)