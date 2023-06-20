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

def solution(s1, s2, dp):
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j][0] = dp[i-1][j-1][0] + 1
                dp[i][j][1] = dp[i-1][j-1][1] + s1[i-1]
            else:
                dp[i][j][0] = max([dp[i-1][j][0], dp[i][j-1][0]])
                dp[i][j][1] = dp[i-1][j][1] if dp[i-1][j][0] > dp[i][j-1][0] else dp[i][j-1][1]
    print(dp[len(s1)][len(s2)][0])
    print(dp[len(s1)][len(s2)][1])
    
            
if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    s1, s2 = input().rstrip(), input().rstrip()
    dp = [[[0, ''] for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    
    # output
    solution(s1, s2, dp)