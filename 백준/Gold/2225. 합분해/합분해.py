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

def solution(n, k):
    memo = [0] * (n+1)
    memo[0] = 1
    for i in range(k):
        for j in range(1, n+1):
            memo[j] += memo[j-1]
    return memo[n] % 1000000000

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, k = map(int, input().split())
    
    # output
    print(solution(n, k))