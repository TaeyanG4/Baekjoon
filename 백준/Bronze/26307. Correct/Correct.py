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

def sol(h, m):
    dhour = 9
    h = h - dhour
    
    return h*60 + m
        
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    h, m = map(int, input().split())
    
    # Output
    print(sol(h, m))

