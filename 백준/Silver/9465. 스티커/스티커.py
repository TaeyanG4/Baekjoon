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

def solution(li):
    for i in range(1, n):
        if i == 1:
            li[0][i] += li[1][i-1]
            li[1][i] += li[0][i-1]
        else:
            li[0][i] += max(li[1][i-1], li[1][i-2])
            li[1][i] += max(li[0][i-1], li[0][i-2])
    return max(li[0][n-1], li[1][n-1])

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    t = int(input())
    for _ in range(t):
        li = list()
        n = int(input())
        for _ in range(2):
            li.append(list(map(int, input().split())))
            
        # output
        print(solution(li))
    
    
    