# import lines
#################################
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
# from itertools import *
# from statistics import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def solution(a, b, c):
    
    # 판별식이 음수면 해가 없다
    if b ** 2 - 4 * a * c < 0:
        return -1
    
    # 모든 a와 c의 약수 조합을 찾는다.
    # 제곱근까지만 찾아도 된다
    factors_a = [(i, a//i) for i in range(1, abs(a)+1) if a % i == 0]
    factors_c = [(i, c//i) for i in range(1, abs(c)+1) if c % i == 0]
    
    # 모든 약수 조합에 대해
    for fa in factors_a:
        for fc in factors_c:
            xa, xb, xc, xd = fa[0], fc[0], fa[1], fc[1]
            if xa * xc == a and xb * xd == c and xa * xd + xb * xc == b:
                return xa, xb, xc, xd
    return -1

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    # INF = sys.maxsize
    
    # input
    n = int(input())
    
    # output
    ans = solution(n, n+1, -(n+2))
    if ans == -1:
        print(-1)
    else:
        print(*ans)