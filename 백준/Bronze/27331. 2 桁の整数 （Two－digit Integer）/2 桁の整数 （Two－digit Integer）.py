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

def sol(a, b):
    s = a + b
    return s
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    a, b = input().strip(), input().strip()
    
    # Output
    print(sol(a, b))