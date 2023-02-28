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

def solution(n, m):
    cnt = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            if (a**2+b**2+m)%(a*b) == 0:
                cnt += 1
    return cnt
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    t = int(input())
    
    # output
    for i in range(t):
        n, m = map(int, input().split())
        print(solution(n, m))