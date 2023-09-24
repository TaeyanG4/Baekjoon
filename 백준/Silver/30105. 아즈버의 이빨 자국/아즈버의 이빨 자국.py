## taeyang's template (1.0.7)
#################################
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################


def solution():
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    # n, m = map(int, input().split())
    
    n = int(input())
    lst = [*map(int, input().split())]
    
    s_lst = set(lst)
    lst_len = len(lst)
    ans = []
    for k in range(lst_len-1):
        gap = lst[k+1] - lst[0]
        visited = set()
        for i in range(lst_len-1):
            if lst[i] + gap in s_lst:
                visited.add(lst[i])
                visited.add(lst[i] + gap)
        
        for i in lst:
            if i not in visited:
                break
        else:
            ans.append(gap)
    
    print(len(ans))
    if ans:
        print(*ans)

    # lst_len = len(lst)
    # ans_lst = []
    # for k in range(lst_len-1):
    #     gap = lst[k+1] - lst[0]
    #     visited = [False] * lst_len
    #     for i in range(lst_len-1):
    #         if all(visited):
    #             break
    #         for j in range(i+1, lst_len):
    #             if lst[j] - lst[i] == gap:
    #                 visited[i] = True
    #                 visited[j] = True
    #                 break
        
    #     if all(visited):
    #         ans_lst.append(gap)
    
    # print(len(ans_lst))
    # if ans_lst:
    #     print(*ans_lst)