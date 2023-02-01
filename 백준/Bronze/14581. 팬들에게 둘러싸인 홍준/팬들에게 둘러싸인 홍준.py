## import line
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

def sol(l):
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    name = input().strip()
    
    # Output
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                print(":"+name+":", end="")
            else:
                print(":fan:", end="")
        print()