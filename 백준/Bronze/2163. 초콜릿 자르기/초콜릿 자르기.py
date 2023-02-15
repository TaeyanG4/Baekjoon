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

def sol(n, m):
    ans = (n-1) + (n*(m-1))
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n, m = map(int, input().split())
    
    # Output
    print(sol(n, m))