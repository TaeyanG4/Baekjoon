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
# from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
# from statistics import *
#################################

def solution():
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    w1, h1, w2, h2 = int(input()), int(input()), int(input()), int(input())
    max_w = max(w1, w2)
    print((h1+h2+max_w)*2+4)