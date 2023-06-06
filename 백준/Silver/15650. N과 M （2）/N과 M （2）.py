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
# import statistics as st
# from decimal import *
from collections import *
from itertools import *
# from heapq import *
# from datetime import datetime
#################################

def solution(n, m):
    temp = []
    for i in range(1, n+1):
        temp.append(i)
    ans = list(combinations(temp, m))
    for i in ans:
        for j in i:
            print(j, end=' ')
        print()

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n, m = map(int, input().split())
    
    # output
    solution(n, m)