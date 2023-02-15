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
    sorted_s = sorted(s, reverse=True)
    if '0' in s and sum(map(int, sorted_s)) % 3 == 0:
        return "".join(sorted_s)
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    s = input().strip()
    
    # Output
    print(sol(s))