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

def sol(n):
    igni = [0, 1]
    
    if n == 0:
        return igni[0]
    elif n == 1:
        return igni[1]
    
    for i in range(2, n+1):
        igni.append(igni[i-1] + igni[i-2])
    return igni[-1]

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())
    
    # Output
    print(sol(n))