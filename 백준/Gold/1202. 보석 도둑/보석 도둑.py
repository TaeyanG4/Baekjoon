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
from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def solution(n, k):
    ans = 0
    pq_info, bags = [], []
    temp = []
    
    for _ in range(n):
        m, v = map(int, input().split())
        heappush(pq_info, (m, -v))
    
    for _ in range(k):
        bags.append(int(input()))
    bags.sort()
    
    for bag in bags:
        while pq_info and bag >= abs(pq_info[0][0]):
            heappush(temp, heappop(pq_info)[1])
        
        if temp:
            ans += abs(heappop(temp))
        elif not pq_info:
            break

    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n, k = map(int, input().split())

    # output
    print(solution(n, k))
