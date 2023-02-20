# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def sol(n, k, li):
    li.sort(reverse=True)
    return li[k-1]
    
if __name__ == '__main__':
    
    # input
    n, k = map(int, input().split())
    li = list(map(int, input().split()))

    # output
    print(sol(n, k, li))
