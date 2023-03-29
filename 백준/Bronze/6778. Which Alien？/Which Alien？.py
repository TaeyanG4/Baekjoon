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

def solution(a, b):
    if a >= 3 and b <= 4:
        print("TroyMartian")
    if a <= 6 and b >= 2:
        print("VladSaturnian")
    if a <= 2 and b <= 3:
        print("GraemeMercurian")

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    a = int(input())
    b = int(input())

    # output
    solution(a, b)