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

def merge_sort(li):
    if len(li) <= 1:
        return li
    
    mid = (len(li)+1) // 2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])
    
    i, j = 0, 0
    arr = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            ans.append(right[j])
            j += 1
    while i < len(left):
        arr.append(left[i])
        ans.append(left[i])
        i += 1
    while j < len(right):
        arr.append(right[j])
        ans.append(right[j])
        j += 1
    return arr

def solution(n, k, li):
    merge_sort(li)
    if len(ans) < k:
        return -1
    else:
        return ans[k-1]

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    ans = []
    
    # output
    print(solution(n, k, li))
