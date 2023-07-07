# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
import pprint
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def solution():
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n = int(input())
    mats = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # output
    for i in range(1, n):
        for j in range(0, n-i):
            if i == 1:
                dp[j][j+i] = mats[j][0] * mats[j][1] * mats[j+i][1]
            else:
                dp[j][j+i] = sys.maxsize
                for k in range(j, j+i):
                    dp[j][j+i] = min(dp[j][j+i], 
                                     dp[j][k] + dp[k+1][j+i] + mats[j][0] * mats[k][1] * mats[j+i][1])
                    
    print(dp[0][n-1])
