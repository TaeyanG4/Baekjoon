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
from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(n, txts):
    dash = '--'
    ans = []
    txts.sort()
    for i in range(n):
        if i == 0:
            for j in range(len(txts[i])):
                ans.append(dash*j + txts[i][j])
        else:
            idx = 0
            for j in range(len(txts[i])):
                if txts[i-1][j] != txts[i][j] or len(txts[i-1]) <= j:
                    break
                else:
                    idx = j + 1
            for j in range(idx, len(txts[i])):
                ans.append(dash*j + txts[i][j])
    
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    txts = [list(input().split())[1:] for _ in range(n)]
    
    # output
    for a in solution(n, txts):
        print(a)