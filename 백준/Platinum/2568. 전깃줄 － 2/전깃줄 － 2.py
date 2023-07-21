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
from bisect import *
#################################

def solution(n, li):
    li_temp = [INF * -1]
    li_idx = [(INF * -1, 0)]
    li = li[::-1]
    
    while li:
        num = li.pop()
        
        if num > li_temp[-1]:
            li_idx.append((num, len(li_temp)))
            li_temp.append(num)
        else:
            idx = bisect_left(li_temp, num)
            li_temp[idx] = num
            li_idx.append((num, idx))
    
    ans_len = len(li_temp) - 1
    ans = []
    
    while li_idx and ans_len:
        num, idx = li_idx.pop()
        
        if idx == ans_len:
            ans.append(num)
            ans_len -= 1
    
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    graph = []
    for _ in range(n):
        a, b = map(int, input().split())
        graph.append([a, b])
    graph.sort()
    li = [temp[1] for temp in graph]
    
    # output
    ans = solution(n, li)
    print(len(graph) - len(ans))
    for num in graph:
        if num[1] not in ans:
            print(num[0])