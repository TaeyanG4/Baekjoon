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

# https://velog.io/@stripe2933/bj11042
# https://suri78.tistory.com/78
# https://johngrib.github.io/wiki/Fermat-s-little-theorem/
# https://blog.naver.com/phc328/223005378921
# https://rhdtka21.tistory.com/123

def power(n, k):
    if k == 1:
        return n
    pow_half = power(n, k//2)
    if k % 2 == 0:
        return pow_half * pow_half % MOD
    else:
        return pow_half * pow_half * n % MOD

def inverse(n):
    return power(factorial[n], 1000000005)

def solution(n, k):
    return factorial[n] * inverse(k) * inverse(n-k) % MOD

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    MOD = 1000000007
    
    # 팩토리얼 미리 구하기
    factorial = [1] * (4000000+1)
    for idx in range(2, 4000000+1):
        factorial[idx] = (factorial[idx-1] * idx) % MOD
    
    # output
    for _ in range(int(input())):
        n, k = map(int, input().split())
        print(solution(n, k))