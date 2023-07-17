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

def solution(n, c, li):
    
    dic = defaultdict(list)
    idx = 0
    for v in li:
        if len(dic[v]) == 0:
            dic[v].append([idx, 1])
            idx += 1
        else:
            temp_idx, temp_cnt = dic.pop(v)[0]
            dic[v].append([temp_idx, temp_cnt+1])
    
    # cnt를 먼저 정렬후 idx를 정렬
    return sorted(dic.items(), key= lambda x: (x[1][0][1], x[1][0][0] * -1), reverse=True)

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, c = map(int, input().split())
    li = map(int, input().split())
    
    # output
    for k, v in solution(n, c, li):
        print((str(k) + ' ') * v[0][1], end='')
    print()