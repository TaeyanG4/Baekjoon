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
from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(n, mat):
    min_val = INF
    for comb in combinations(range(n), n//2):
        team_link, team_start = 0, 0
        for i in range(n):
            if i in comb:
                team_link += sum([mat[i][j] for j in comb if i != j])
            if i not in comb:
                team_start += sum([mat[i][j] for j in range(n) if j not in comb and i != j])
        min_val = min(min_val, abs(team_link - team_start))
    return min_val

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    
    # output
    print(solution(n, mat))