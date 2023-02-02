# import line
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

def sol(a, b):
    if 100.0 <= a-a*b/100:
        return 0
    else:
        return 1

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    a, b = map(int, input().split())

    # Output
    print(sol(a, b))