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

def dfs(n):
    if n == 0:
        return 1
    
    if n in dp:
        return dp[n]
    
    dp[n] = dfs(n//p) + dfs(n//q)
    
    return dp[n]

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, p, q = map(int, input().split())
    dp = defaultdict(int)
    dp[0] = 1
    
    # output
    dfs(n)
    print(dp[n])
