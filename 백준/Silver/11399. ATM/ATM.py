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

def sol(order):
    sum_all = 0
    order.sort()
    for i in range(len(order)+1):
        sum_all += sum(order[0:i])
    return sum_all

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())
    order = list(map(int, input().split()))
    
    # Output
    print(sol(order))
