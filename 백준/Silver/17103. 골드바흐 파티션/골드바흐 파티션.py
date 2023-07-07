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
# from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
# from statistics import *
#################################

def eratos_sieves(n):
    prime = [True] * (n+1)
    prime[0], prime[1] = [False], [False]
    for i in range(2, int(math.sqrt(n))+1):
        if prime[i]:
            for j in range(i+i, n+1, i):
                prime[j] = False
    return prime

def solution(n):
    ans = 0
    for i in range(2, (n//2)+1):
        if sieves[i] and sieves[n-i]:
            ans += 1
    return ans
    
if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    t = int(input())
    sieves = eratos_sieves(10**6)
    for _ in range(t):
        n = int(input())
        print(solution(n))