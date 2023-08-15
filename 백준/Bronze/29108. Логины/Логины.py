## taeyang's template (1.0.0)
#################################
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import time
# import pprint
# from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(s):
    if len(s) <= 2:
        return 'Incorrect'
    if s[0] != 'i':
        return 'Incorrect'
    if s[1] != 'o':
        return 'Incorrect'
    for c in s[2:]:
        if not c.isdigit():
            return 'Incorrect'
    return 'Correct'

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    s = input().rstrip()
    
    # output
    print(solution(s))