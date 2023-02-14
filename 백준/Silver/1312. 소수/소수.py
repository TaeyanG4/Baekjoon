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

def sol(a, b, n):
    for _ in range(n):
        a = (a%b)*10
        ans = a//b
    return ans 
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    a, b, n = map(int, input().split())
    
    # Output
    print(sol(a, b, n))