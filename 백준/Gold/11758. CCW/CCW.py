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
# from itertools import *
# from datetime import datetime
#################################

def solution(node):
    x1, y1 = node[0]
    x2, y2 = node[1]
    x3, y3 = node[2]
    res = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    node = []
    for _ in range(3):
        node.append(list(map(int, input().split())))
    
    # ouput
    print(solution(node))
