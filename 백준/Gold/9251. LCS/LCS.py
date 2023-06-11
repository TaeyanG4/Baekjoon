# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
# from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
#################################

def solution(a, b, dp):
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(a)][len(b)]

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    a = input().strip()
    b = input().strip()
    dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    
    # ouput
    print(solution(a, b, dp))