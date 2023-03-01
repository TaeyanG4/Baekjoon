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

def solution(li):
    sum_score = 0.0
    grade = 0.0
    for record in li:
        if record[2] == 'A+':
            grade += 4.5 * float(record[1])
            sum_score += float(record[1])
        elif record[2] == 'A0':
            grade += 4.0 * float(record[1])
            sum_score += float(record[1])
        elif record[2] == 'B+':
            grade += 3.5 * float(record[1])
            sum_score += float(record[1])
        elif record[2] == 'B0':
            grade += 3.0 * float(record[1])
            sum_score += float(record[1])
        elif record[2] == 'C+':
            grade += 2.5 * float(record[1])
            sum_score += float(record[1])
        elif record[2] == 'C0':
            grade += 2.0 * float(record[1])
            sum_score += float(record[1])
        elif record[2] == 'D+':
            grade += 1.5 * float(record[1])
            sum_score += float(record[1])
        elif record[2] == 'D0':
            grade += 1.0 * float(record[1])
            sum_score += float(record[1])
        elif record[2] == 'F':
            grade += 0.0 * float(record[1])
            sum_score += float(record[1])
        
    return grade / sum_score
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    li = list() 
    for _ in range(20):
        li.append(tuple(map(str, input().split())))

    # output
    print(solution(li))