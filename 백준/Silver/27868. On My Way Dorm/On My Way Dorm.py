# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import json
import pprint
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def solution(cmd):
    return cmd[::-1]


if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n, s = map(int, input().split())
    li = list(map(int, input().split()))
    cmd = input().strip()

    # output
    print(solution(cmd))