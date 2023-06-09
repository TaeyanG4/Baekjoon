# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
# import statistics as st
# from decimal import *
from collections import *
from itertools import *
# from heapq import *
# from datetime import datetime
#################################

def solution(n, li):
    for i in range(1, n):
        li[i][0] = min(li[i-1][1], li[i-1][2]) + li[i][0]
        li[i][1] = min(li[i-1][0], li[i-1][2]) + li[i][1]
        li[i][2] = min(li[i-1][0], li[i-1][1]) + li[i][2]
    return min(li[n-1][0], li[n-1][1], li[n-1][2])

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = int(input())
    li = []
    for i in range(n):
        li.append(list(map(int, input().split())))
    
    # output
    print(solution(n, li))
    