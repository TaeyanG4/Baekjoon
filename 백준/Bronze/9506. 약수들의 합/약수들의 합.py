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

def solution(n):
    cm = list()
    for i in range(1,n):
        if n % i == 0:
            cm.append(i)
    if sum(cm) == n:
        print(f"{n} = ", end = "")
        print(" + ".join([str(i) for i in cm]))
    else:
        print(f"{n} is NOT perfect.")
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    # n = int(input())

    # output
    while True:
        n = int(input())
        if n == -1:
            break
        solution(n)