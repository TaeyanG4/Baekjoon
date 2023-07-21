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

def solution(state):
    temp = [0] * 8
    temp[0] = state[1] + state[2] # 정보과학관
    temp[1] = state[0] + state[2] + state[3] # 전산관
    temp[2] = state[0] + state[1] + state[3] + state[4] # 미래관
    temp[3] = state[1] + state[2] + state[4] + state[5] # 신양관
    temp[4] = state[2] + state[3] + state[5] + state[7] # 한경직기념관
    temp[5] = state[3] + state[4] + state[6] # 진리관
    temp[6] = state[5] + state[7] # 학생회관
    temp[7] = state[4] + state[6] # 형남공학관
    
    for i in range(8):
        temp[i] %= 1000000007
        
    return temp



if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    dp = [1, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(int(input())):
        dp = solution(dp)
    
    # output
    print(dp[0])