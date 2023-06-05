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
# import statistics as st
# from decimal import *
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
#################################

# direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def checking(a, b, c):
    dist = 0
    for i in range(4):
        if a[i] != b[i]:
            dist += 1
        if b[i] != c[i]:
            dist += 1
        if c[i] != a[i]:
            dist += 1
    
    return dist

def solution(n, mbti):
    min_val = 10000000000
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                min_val = min(min_val, checking(mbti[i], mbti[j], mbti[k]))
                if min_val == 0:
                    break
    
    return min_val

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        mbti = input().rstrip().split()
        # output
        if n > 32:
            print(0)
        else:
            print(solution(n, mbti))
