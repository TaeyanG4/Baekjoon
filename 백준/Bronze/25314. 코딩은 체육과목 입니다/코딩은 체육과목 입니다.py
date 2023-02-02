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

def sol(n):
    for i in range(n//4):
        print("long", end=' ')
    print("int")
        
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())

    # Output
    sol(n)