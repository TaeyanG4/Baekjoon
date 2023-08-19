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

def solution(n, roads, oil_prices):
    ans = 0
    min_price = INF
    for i in range(n-1):
        min_price = min(min_price, oil_prices[i])
        ans += min_price * roads[i]
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    roads = list(map(int, input().split()))
    oil_prices = list(map(int, input().split()))
    
    # output
    print(solution(n, roads, oil_prices))