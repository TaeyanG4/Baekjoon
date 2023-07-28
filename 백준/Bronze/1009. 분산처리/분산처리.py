# import lines
#################################
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

def solution(a, b):
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    t = int(input())
    
    # output
    for _ in range(t):
        a, b = map(int, input().split())
        val = a
        temp = []
        while True:
            if len(temp) > 1 and temp[-1] == temp[0]:
                break
            if val % 10 == 0:
                temp.append(10)
            else:
                temp.append(val%10)
            val = val*a
        temp.pop()
        mod = b % len(temp)
        print(temp[mod-1])