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
from collections import *
from heapq import *
# from itertools import *
# from datetime import datetime
#################################

def reverse(arr, s, e):
    c = (e - s + 1) // 2
    for i in range(c):
        arr[s+i], arr[e-i] = arr[e-i], arr[s+i]
    return arr
        
def front(li, s, e):
    cnt = 0
    arr_f = copy.deepcopy(li)
    while s != e:
        for i in range(s, e+1):
            if s == arr_f[s]:
                break
            if arr_f[i] == s:
                arr_f = reverse(arr_f, s, i)
                cnt += 1
                res1.append((s, i))
        s += 1
        
    if cnt == 1:
        res1.append((1, 1))
        return True
    elif cnt == 2:
        return True
    else:
        return False

def back(li, s, e):
    cnt = 0
    arr_b = copy.deepcopy(li)
    while s != e:
        for i in range(s, e-1, -1):
            if s == arr_b[s]:
                break
            if arr_b[i] == s:
                arr_b = reverse(arr_b, i, s)
                cnt += 1
                res2.append((i, s))
        s -= 1
        
    if cnt == 1:
        res2.append((1, 1))
    elif cnt == 2:
        pass
    else:
        res2.append((1, 1))
        res2.append((1, 1))

def solution(li):
    if front(li, 1, n):
        return True
    else:
        back(li, n, 1)
        return False

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n = int(input())
    li = [0] + list(map(int, input().split()))
    res1, res2 = [], []
    
    # ouput
    if solution(li):
        for i in res1:
            print(*i)
    else:
        for i in res2:
            print(*i)