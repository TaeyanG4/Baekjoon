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

def solution(n, seq):
    res = [0]*n
    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp_incre[i] = max(dp_incre[i], dp_incre[j] + 1)
            if reverse_seq[i] > reverse_seq[j]:
                dp_decre[i] = max(dp_decre[i], dp_decre[j] + 1)
    
    for i in range(n):
        res[i] = dp_incre[i] + dp_decre[n-i-1] - 1
    return max(res)

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n = int(input())
    seq = list(map(int, input().split()))
    reverse_seq = seq[::-1]
    dp_incre, dp_decre = [1]*n, [1]*n
    
    # output
    print(solution(n, seq))
