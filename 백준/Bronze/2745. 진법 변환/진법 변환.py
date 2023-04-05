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
# import statistics as st
# from decimal import *
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
#################################

def solution(n, b):
    ans = 0
    li = list(n)
    for i in range(0, len(n)):
        temp = li.pop()
        if temp.isdigit():
            ans += int(temp) * (int(b) ** i)
        else:
            ans += (ord(temp) - 55) * (int(b) ** i)
    
    return ans
    
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n, b = map(str, input().split())
    
    # output
    print(solution(n, b))



