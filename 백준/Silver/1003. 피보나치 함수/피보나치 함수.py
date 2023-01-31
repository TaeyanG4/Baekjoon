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

def fibonacci(n):
    zeros=[1,0,1]
    ones=[0,1,1]
    if n > 2:
        for i in range(2,n):
            zeros.append(zeros[i-1] + zeros[i])
            ones.append(ones[i-1] + ones[i])
    return zeros[n], ones[n]

def sol():
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    t = int(input())
    
    # Output
    for i in range(t):
        n = int(input())
        zero, one = fibonacci(n)
        print(zero, one)