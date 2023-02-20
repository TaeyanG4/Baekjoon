# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import json
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def sol(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return sol(n-1) + sol(n-2)

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n = int(input())
    
    # output
    print(sol(n))