## taeyang's template (1.0.1)
#################################
## my import lines
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
# from itertools import *
# from statistics import *
from datetime import *
# from bisect import *
#################################

def solution(today_nyam, tomorrow_nyam):
    gap = tomorrow_nyam - today_nyam
    h, m = divmod(gap.seconds // 60, 60)
    if today_nyam < tomorrow_nyam:
        return h+24, m
    else:
        return h, m

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    today_nyam = datetime.strptime(input().rstrip(), '%H:%M')
    tomorrow_nyam = datetime.strptime(input().rstrip(), '%H:%M')
    
    # output
    h, m = solution(today_nyam, tomorrow_nyam)
    print(f"{h:02d}:{m:02d}")