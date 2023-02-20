# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def sol(val):
    return st.mean(val), st.median(val)
    
if __name__ == '__main__':
    
    # input
    val = [int(input()) for _ in range(5)]

    # output
    ans = sol(val)
    print(ans[0])
    print(ans[1])
