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

def sol():
    pass
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    
    # Output
    cnt = 1
    while True:
        val = [int(x) for x in input().split()]
        if val[0] == 0:
            break
        print(f"Case {cnt}: Sorting... done!")
        cnt += 1