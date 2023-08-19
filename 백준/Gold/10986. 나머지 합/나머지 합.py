## taeyang's template (1.0.1)
# https://only-wanna.tistory.com/entry/파이썬-백준-10986번-나머지-합
# https://beluga9.tistory.com/405
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
from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
#################################

def solution(li):
    
    remain = [0] * m
    li.append(0)
    for i in range(n):
        li[i] += li[i-1]
        remain[li[i] % m] += 1
    
    ans = remain[0]
    for v in remain:
        # prefix_sum에서 m으로 나누어 떨어진수를 저장한 remain에서 2개를 뽑는다.
        # 똑같은 나머지 a, b를 뺴면 나머지가 0이되기 떄문이다.
        ans += math.comb(v, 2) # nC2; n개 중 2개를 뽑는 경우의 수
    
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    
    # output
    print(solution(li))