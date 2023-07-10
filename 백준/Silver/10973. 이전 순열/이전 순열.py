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

def solution(n, li):
    for i in range(n-1, 0, -1):
        if li[i-1] > li[i]:
            for j in range(n-1, 0, -1):
                if li[i-1] > li[j]:
                    li[i-1], li[j] = li[j], li[i-1]
                    li = li[:i] + sorted(li[i:], reverse=True)
                    return li
    else:
        return [-1]
    
if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n = int(input())
    li = list(map(int, input().split()))
    
    # output
    print(*solution(n, li))
