# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import json
import pprint
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def solution(n):
    if n == 0: return 0
    if n == 1: return 1
    
    memo = [0, 1]
    
    for i in range(2, n+1):
        memo[0], memo[1] = memo[1], memo[0] + memo[1]

    return memo[1]
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n = int(input())

    # output
    print(solution(n))
