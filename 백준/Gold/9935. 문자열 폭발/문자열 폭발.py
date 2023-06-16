# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################

def solution(s, boom):
    stack = []
    for c in s:
        stack.append(c)
        if c in boom:
            while ''.join(stack[-len(boom):]) == boom:
                del stack[-len(boom):]
    return ''.join(stack) if stack else 'FRULA'
    

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    s = input().strip()
    boom = input().strip()

    # output
    print(solution(s, boom))
