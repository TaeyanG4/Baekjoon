# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################

def solution(n, li):
    check = [False] * 1000001
    score = [0] * 1000001
    
    for i in range(n):
        check[li[i]] = True
    
    for val in li:
        j = val * 2
        while j <= 1000000:
            if check[j] == True:
                score[val] += 1
                score[j] -= 1
            j += val
    
    return score
    
if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n = int(input())

    li = list(map(int, input().split()))
    
    # output
    ans = solution(n, li)
    for idx in li:
        print(ans[idx], end=' ')
    print()