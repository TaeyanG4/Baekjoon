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

def sol():
    
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        
        if a < b and b % a == 0:
            print('factor')
        elif a > b and a % b == 0:
            print('multiple')
        else:
            print('neither')
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    
    # output
    sol()
