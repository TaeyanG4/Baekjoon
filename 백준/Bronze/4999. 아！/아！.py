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
    a, b = input(), input()
    
    # Output
    print("go") if len(a) >= len(b) else print("no")