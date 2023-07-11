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

def solution(n, m, s):
    last, a1, a2 = '', '', ''
    vowel = ['A', 'E', 'I', 'O', 'U']
    while s and s[-1] in vowel:
        s.pop()
    if s:
        last = s.pop()
    
    while s and s[-1] != 'A':
        s.pop()
    if s:
        a1 = s.pop()
    
    while s and s[-1] != 'A':
        s.pop()
    if s:
        a2 = s.pop()

    new_s = s + [a2, a1, last]
    
    if len(new_s) > m:
        return 'YES'
    else:
        return 'NO'
    

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n, m = map(int, input().split())
    s = list(input().strip())
    
    # output
    print(solution(n, m, s))
