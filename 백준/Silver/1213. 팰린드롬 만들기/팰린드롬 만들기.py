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
from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(s, dic):
    odd_cnt = 0
    center = ''
    for i, v in dic.items():
        if v % 2 == 1:
            odd_cnt += 1
            center = i
            if odd_cnt >= 2:
                return "I'm Sorry Hansoo"
    
    dic = sorted(dic.items(), key=lambda x: x[0])
    
    ans = ''
    for i, v in dic:
        ans += i * (v // 2)
    temp = ans[::-1]
    ans += center 
    ans += temp
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    s = list(input().rstrip())
    dic = defaultdict(int)
    for c in s:
        dic[c] += 1

    # output
    print(solution(s, dic))