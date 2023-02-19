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

def sol(set_a, set_b):
    return set_a - set_b
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    a, b = map(int, input().split())
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    
    # Output
    ans = sol(set_a, set_b)
    print(len(ans))
    print(*sorted(ans))