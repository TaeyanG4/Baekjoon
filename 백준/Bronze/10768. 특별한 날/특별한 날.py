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

def solution(m, d):
    if m > 2:
        return "After"
    elif m < 2:
        return "Before"
    else:
        if d > 18:
            return "After"
        elif d < 18:
            return "Before"
        else:
            return "Special"

    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    m = int(input())
    d = int(input())
    
    # output
    print(solution(m, d))


