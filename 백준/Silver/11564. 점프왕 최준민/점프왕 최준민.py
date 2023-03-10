# import lines
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

def sol(k, a, b):
    start = (a-1) // k
    end = b // k
    return end-start

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    k, a, b = map(int, input().split())
    
    # Output
    print(sol(k, a, b))