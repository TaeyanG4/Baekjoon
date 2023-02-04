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

def sol(a, b, c):
    perfomance = b//a
    war_performance = perfomance*3*c
    return int(war_performance)
        
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    a, b, c = map(int, input().split())
    
    # Output
    print(sol(a, b, c))
