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

def solution(li):
    ans = list()
    for i in range(0,16):
        for j in range(0,5):
            try:
                ans.append(li[j][i])
            except:
                pass
    return "".join(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    li = [input().strip() for _ in range(5)]

    # output
    print(solution(li))
