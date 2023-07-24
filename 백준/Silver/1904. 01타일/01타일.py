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

def solution(n):
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    memo = [0] * (n+1)
    memo[1] = 1
    memo[2] = 2

    for i in range(3, n+1):
        memo[i] = memo[i-1] % 15746 + memo[i-2] % 15746
    
    return memo[n] % 15746


if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    
    
    # output
    print(solution(n))