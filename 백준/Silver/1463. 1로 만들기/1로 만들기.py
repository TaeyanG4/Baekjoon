## import line
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

def sol(x):
    d = [0] * (x + 1)
    for i in range(2, x + 1):
        # -1
        d[i] = d[i - 1] + 1
        
        # 1/3 
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
            
        # 1/2 
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)  
    return d[x]

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    x = int(input())
    
    # Output
    print(sol(x))