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

def solution(left, right, both):
    while True:
        if left == right:
            return 2 * (left + both//2)
        
        if left < right:
            left += 1
            both -= 1
        elif left > right:
            right += 1
            both -= 1
        
        if both == 0:
            return min(left, right) * 2
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    left, right, both = map(int, input().split())


    # output
    print(solution(left, right, both))
