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

def sol(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

        return 2
    a, b = 1, 2
    for i in range(n-2):
        a, b = b, (a+b)%10007
    return b

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())
    
    # Output
    print(sol(n))
