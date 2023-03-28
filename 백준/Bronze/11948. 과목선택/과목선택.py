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
    a.sort()
    b.sort()
    return sum(a[1:]) + sum(b[1:])

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    a = [int(input()) for _ in range(4)]
    b = [int(input()) for _ in range(2)]

    # output
    print(solution(a, b))