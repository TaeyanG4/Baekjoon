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

def sol(a, b, score):
    sum_a = 0
    sum_b = 0
    for i in range(len(score)):
        sum_a += a[i] * score[i]
    for i in range(len(score)):
        sum_b += b[i] * score[i]
    return sum_a, sum_b
        
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    score = [6,3,2,1,2]
    
    # Output
    ans = sol(a, b, score)
    print(ans[0], ans[1])
