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

def sol(n):
    if n<25:
        print(n//5)
    elif n<125:
        print(n//5+n//25)
    else:
        print(n//5+n//25+n//125)

if __name__ == '__main__':
    input = sys.stdin.readline
    
    n = int(input().strip())
    sol(n)