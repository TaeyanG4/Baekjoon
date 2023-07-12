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
# from itertools import *
# from statistics import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

# https://devlibrary00108.tistory.com/157

def solution(n):
    # 비트 정보, 자릿 수 ,끝나는 수
    dp = [[[0]*10 for _ in range(101)] for _ in range(1<<10)]
    
    # 시작값 초기화
    for i in range(1, 10):
        dp[1<<i][0][i] = 1
        
    # 자릿수 n만큼 순회
    for i in range(1, n):
        # 0~9 까지 순회
        for e in range(10):
            # 비트마스크 순회
            for bm in range(1<<10):
                if e < 9:
                    dp[bm|(1<<e)][i][e] += dp[bm][i-1][e+1] % MOD
                if e > 0:
                    dp[bm|(1<<e)][i][e] += dp[bm][i-1][e-1] % MOD
    
    # 111111111(1023)다 켜지고 자릿수가 n인 dp의 값을 모두 더하기
    return sum(dp[(1<<10)-1][n-1]) % MOD

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n = int(input())
    MOD = 1000000000

    # output
    print(solution(n))