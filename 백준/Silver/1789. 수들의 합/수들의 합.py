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
    i = 1
    while i*(i+1)/2 <= s:
        i += 1
    return i-1
            

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    s = int(input())
    
    # Output
    print(sol(s))