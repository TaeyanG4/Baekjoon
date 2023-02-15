# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def sol(li):
    cnt = 0
    max_h = 0
    for _ in range(len(li)):
        val = li.pop()
        if val > max_h:
            max_h = val
            cnt += 1
    return cnt
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())
    li = [int(input()) for _ in range(n)]

    
    # Output
    print(sol(li))