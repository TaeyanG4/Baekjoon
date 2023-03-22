# import line
#################################
import sys
import math
import copy
import ast
import re
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
from pprint import *
#################################

def solution(n):
    dic = defaultdict(list)
    for _ in range(n):
        v1, v2 = input().split()
        dic[v2].append(v1)
    
    # 모든 의류 종류의 의류 수에 대해, (의류 수 + 1) 서로 싹 다 곱해주고 -1
    res = 1
    for v in dic.keys():
        res *= len(dic[v]) + 1
    return res - 1

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    t = int(input())
    
    # output
    for i in range(t):
        n = int(input())
        print(solution(n))