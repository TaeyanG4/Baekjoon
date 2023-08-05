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

def solution(n, k, coins):
    memo = [0] * (k + 1)
    memo[0] = 1
    for coin in coins:
        for i in range(coin, k + 1):
            memo[i] += memo[i - coin]
    return memo[k]

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    
    # output
    print(solution(n, k, coins))