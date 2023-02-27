# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import json
import pprint
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def solution(n, m, words, tests):
    dic = {}
    cnt = 0
    
    for word in words:
        for i in range(1 + len(word)):
            dic[word[:i]] = 1
    
    for t in tests:
        try:
            cnt += dic[t]
        except KeyError:
            pass
    
    return cnt
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n, m = map(int, input().split())
    words = [input().strip() for i in range(n)]
    tests = [input().strip() for i in range(m)]
    
    # output
    print(solution(n, m, words, tests))