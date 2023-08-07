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
from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

# https://0902.tistory.com/60
# https://sosoeasy.tistory.com/346
# https://0902.tistory.com/60

# failed
# def solution(n, li):
#     ans = 0
#     for i in range(2, n+1):
#         for combi in combinations(li, i):
#             ans += abs(min(combi) - max(combi))
#     return ans

def solution(n, li):
    
    # 모든 조합에서 (조합 안에서 최대값 - 조합 안에서 최소값)을 구해서 더하면 됨
    # [2, 5, 8] 예시 2*(1-4) + 5*(2-2) + 8*(4-1) = 18
    
    ans = 0
    for i in range(n):
        ans += li[i] * (pow(2, i) - pow(2, n-i-1))
    return ans % 1000000007

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    
    # input
    n = int(input())
    li = sorted(map(int, input().split()))
    
    # output
    print(solution(n, li))