# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
# import statistics as st
# from decimal import *
from collections import *
from itertools import *
# from heapq import *
# from datetime import datetime
#################################

def divv(n):
    if n == 1:
        return a % c
    else:
        temp = divv(n // 2)
        if n % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c
        
# def solution(a, b, c):
#     return divv(b)

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    a, b, c = map(int, input().split())
    
    # output
    print(divv(b))
    