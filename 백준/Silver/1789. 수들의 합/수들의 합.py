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

def sol(s):
    if s == 1 or s == 2:
        return 1
    elif s == 3:
        return 2
    
    sum_value = 0
    for i in range(0, s):
        sum_value += i
        if sum_value > s:
            return i-1

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    s = int(input())
    
    # Output
    print(sol(s))