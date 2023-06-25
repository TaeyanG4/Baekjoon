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

def solution(n, li):
    memo = [1] * n
    for i in range(n):
        for j in range(i):
            if li[i][1] > li[j][1] :
                memo[i] = max(memo[i], memo[j]+1)
    return max(memo)

if __name__ == '__main__':
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    
    # input
    n = int(input())
    li = [tuple(map(int, input().split())) for _ in range(n)]
    li.sort()
    
    # output
    print(n - solution(n, li))