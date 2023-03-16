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

def solution(n):
    li = [0,1,1,1,2,2]
    for i in range(6, n+1):
        li.append(li[i-5]+li[i-1])
    
    return li[n]

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    t = int(input())

    # output
    for i in range(t):
        n = int(input())
        print(solution(n))