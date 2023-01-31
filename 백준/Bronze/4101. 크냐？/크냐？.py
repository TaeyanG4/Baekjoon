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

def sol():
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    
    # Output
    while True:
        a, b = map(int, input().strip().split())
        if a == 0 and b == 0:
            break
        elif a>b:
            print("Yes")
        else:
            print("No")