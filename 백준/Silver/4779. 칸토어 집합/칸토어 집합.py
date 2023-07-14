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
# from itertools import *
# from statistics import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def solution(s, e):
    if e-s == 1:
        return
    else:
        temp = (e-s)//3
        for i in range(s+temp, e-temp):
            memo[i] = ' '
        solution(s, s+temp)
        solution(e-temp, e)

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    # INF = sys.maxsize
    
    while True:
        try:
            # input
            n = int(input())
            memo = ['-'] * (3**n)
            
            # output
            solution(0, len(memo))
            print(''.join(memo))
        except:
            break