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
from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(n, li):
    ans = 0
    for idx, num in enumerate(li):
        
        # num을 제외한 temp_li를 만든다.
        temp_li = []
        temp_li.extend(li)
        temp_li.remove(num)
        
        # 맨 왼쪽 temp_li[0], 맨 오른쪽 temp_li[n-2]
        s, e = 0, n-2
        while s < e:
            sum_val = temp_li[s] + temp_li[e]
            if sum_val < num:
                s += 1
            elif sum_val > num:
                e -= 1
            elif sum_val == num: # 좋은 수가 있으면 +1하고 break
                ans += 1
                break
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    li = sorted(map(int, input().split()))
    
    # output
    print(solution(n, li))