# import line
#################################
import sys
# import math
# import copy
# import ast
# import re
# import statistics as st
# from decimal import *
# from collections import *
# from itertools import *
# from heapq import *
#################################

def sol(d, f, p):
    val = round((float(d)*float(f)*float(p)),2)
    return f"${val:.2f}"
    
        
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    t = int(input())
    
    # Output
    for _ in range(t):
        d, f, p = map(str, input().split())
        print(sol(d, f, p))
