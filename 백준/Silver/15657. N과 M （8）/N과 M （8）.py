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

def solution(start, cnt):
    if cnt == m:
        print(*temp)
        return
    for i in range(start, n):
        temp.append(li[i])
        solution(i, cnt+1)
        temp.pop()
            
    
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort()
    cnt, temp = 0, []
    
    # output
    solution(0, 0)
    