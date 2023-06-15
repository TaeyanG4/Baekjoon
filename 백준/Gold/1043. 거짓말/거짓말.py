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
from itertools import *
# from datetime import datetime
#################################

def solution(knowList):
    parties = []
    for _ in range(m):
        parties.append(set(input().split()[1:]))

    for _ in range(m):
        for party in parties:
            if knowList & party:
                knowList = knowList.union(party)

    cnt = 0
    for party in parties:
        if party & knowList:
            continue
        cnt += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n, m = map(int, input().split())
    knowList = set(input().split()[1:])
    
    # output
    print(solution(knowList))
