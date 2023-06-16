# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################
# https://blog.naver.com/phc328/223005378921
# https://casterian.net/math/FlT.html

def mul(a, b):
    if b == 1:
        return a%X
    if b%2 == 0:
        tmp = mul(a, b//2)
        return (tmp*tmp)%X
    else:
        return a*mul(a, b-1)%X

def solution(n, s):
    # b^(-1) × b ≡ 1(mod X) 일 때, b^(X - 2) ≡ b^(-1) (mod X) 이다.
    return s*mul(n,X-2)%X

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    m = int(input())
    X = 1000000007
    
    # output
    ans = 0
    for _ in range(m):
        n, s = map(int, input().split())
        ans += solution(n, s)
        ans %= X
    print(ans)
