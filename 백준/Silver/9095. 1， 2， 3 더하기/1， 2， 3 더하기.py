# import line
#################################
import sys
import math
import copy
import ast
import re
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def sol(v):
    if v == 1:
        return 1
    elif v == 2:
        return 2
    elif v == 3:
        return 4
    
    dp = [0] * (v+1)
    dp[0], dp[1], dp[2] = 1, 2, 4
    i=0
    while True:
        if v-3 == i:
            return dp[i+2]
        else:
            dp[i+3] = dp[i] + dp[i+1] + dp[i+2]
            i += 1

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    t = int(input())
    
    # Output
    for _ in range(t):
        print(sol(int(input())))
