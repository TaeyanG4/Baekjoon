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

def sol(n, score):
    log = []
    if n == 1:
        return score[0]
    elif n == 2:
        return score[0]+score[1]
    elif n == 3:
        return max(score[1]+score[2], score[0]+score[2])
    else:
        log.append(score[0])
        log.append(score[0]+score[1])
        log.append(max(score[1]+score[2], score[0]+score[2]))
        
    for i in range(3, n):
        log.append(max(score[i]+log[i-2], score[i]+score[i-1]+log[i-3]))
    return log[-1]

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())
    score = [int(input()) for _ in range(n)]
    
    # Output
    print(sol(n, score))
