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
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(n, k, c ,li):
    
    # Ai 를 K로 나눈 나머지가 j인 것의 개수를 Cj라고 한다.
    for i in li:
        c[i%k] += 1
    
    ans = 1
    for i in range(1, (k+1) // 2):
        ans = ans * (pow(2, c[i], MOD) + pow(2, c[k-i], MOD) - 1) % MOD
    
    ans = ans * (c[0] + 1) % MOD
    if k % 2 == 0:
        ans = ans * (c[k//2] + 1) % MOD
    ans = (ans - (n + 1)) % MOD
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, k = map(int, input().split())
    c = [0] * k
    li = list(map(int, input().split()))
    
    # output
    print(solution(n, k, c ,li))