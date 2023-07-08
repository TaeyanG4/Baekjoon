# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def solution(n):
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n, m = map(int, input().split())
    dic = defaultdict(int)
    
    # output
    for _ in range(n):
        s = input().rstrip()
        if len(s) >= m:
            dic[s] += 1
    
    li = list(dic.items())
    li.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
    
    for i in li:
        print(i[0])
