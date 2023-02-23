# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import json
import pprint
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def sol(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return 0
    else:
        return 1
    

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    s = input().strip()
    
    # output
    print(sol(s))
