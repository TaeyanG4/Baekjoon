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
    pass
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n = int(input())
    for i in range(1, n+1):
        print(' '*(n-i) + '*'*(2*i-1))
    for i in range(n-1, 0, -1):
        print(' '*(n-i) + '*'*(2*i-1))