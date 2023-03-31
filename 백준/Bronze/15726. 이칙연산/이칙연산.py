# import lines
#################################
import sys
# import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
# import statistics as st
# from decimal import *
# from collections import *
# from itertools import *
# from heapq import *
#################################

def solution(li):
    return li[0] * max(li[1], li[2]) // min(li[1], li[2]) 

if __name__ == '__main__':
    input = sys.stdin.readline

    li = list(map(int, input().strip().split()))
    
    print(solution(li))

