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
from itertools import *
# from statistics import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

# https://c4u-rdav.tistory.com/61

def solution(n, s, li):
    
    # 반으로 나누기
    left_li = li[:n//2]
    right_li = li[n//2:]
    left_sum, right_sum = [], []
    
    # 왼쪽과 오른쪽 수열의 부분 수열 합 저장
    for i in range(len(left_li)+1):
        for comb in combinations(left_li, i):
            left_sum.append(sum(comb))
    
    for i in range(len(right_li)+1):
        for comb in combinations(right_li, i):
            right_sum.append(sum(comb))
    
    # 투포인터 사용을위해 각각 오름차순과 내림순으로 정렬
    left_sum.sort()
    right_sum.sort(reverse=True)
    left_len, right_len = len(left_sum), len(right_sum)
    
    ans = 0
    lt, rt = 0, 0
    while lt < left_len and rt < right_len:
        lp, rp = left_sum[lt], right_sum[rt]
        t_sum = lp + rp
        
        # 합이 s와 같은경우
        if t_sum == s:
            tlt, trt = lt, rt
            
            # 같은 값이 있는 동안 포인터 증가 하여 중복값 확인
            while tlt < left_len and left_sum[tlt] == lp:
                tlt += 1
            while trt < right_len and right_sum[trt] == rp:
                trt += 1
            ans += (tlt-lt) * (trt-rt)
            lt, rt = tlt, trt
        elif t_sum < s:
            lt += 1
        else:
            rt += 1
    
    if s == 0:
        return ans - 1
    else:
        return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n, s = map(int, input().split())
    li = list(map(int, input().split()))
    
    # output
    print(solution(n, s, li))