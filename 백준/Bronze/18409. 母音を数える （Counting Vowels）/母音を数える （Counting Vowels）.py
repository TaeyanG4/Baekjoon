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
from pprint import *
#################################

def solution(n, s):
    cnt = 0
    for c in s:
        if c in 'aeiou':
            cnt += 1
            
    return cnt
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n = int(input())
    s = input().strip()
        
    # output
    print(solution(n, s))