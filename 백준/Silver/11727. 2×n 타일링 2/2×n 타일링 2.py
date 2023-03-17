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
    li = [1,3,5]
    for i in range(3,n+1):
        li.append(li[-1]+li[-2]*2)
    
    return li[n-1]%10007

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n = int(input())

    # output
    print(solution(n))