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

def sol(time, drink):
    if time >= 12 and time <= 16 and drink == 0:
        return 320
    else:
        return 280
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    time, drink = map(int, input().split())
    
    # Output
    print(sol(time, drink))
