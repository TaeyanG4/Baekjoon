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

def solution(a, b):
    gcd = list()
    for i in range(1,a+1):
        if a % i == 0:
            gcd.append(i)
    try:
        return gcd[b-1]
    except:
        return 0

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    a, b = map(int, input().split())

    # output
    print(solution(a, b))