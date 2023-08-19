## taeyang's template (1.0.1)
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
# from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
#################################

def solution(s, keyword):
    new_s = ''
    for c in s:
        if c.isalpha():
            new_s += c
    
    for i in range(len(new_s) - len(keyword) + 1):
        word = new_s[i:i+len(keyword)]
        if word == keyword:
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    s = input().rstrip()
    keyword = input().rstrip()
    
    # output
    print(solution(s, keyword))