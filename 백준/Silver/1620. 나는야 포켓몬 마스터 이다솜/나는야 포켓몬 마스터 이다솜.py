import sys
import math
import copy
import ast
import re
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *

class MyClass:
    def __init__(self):
        self.dict = {}

    def sol(self, input_value):
        if input_value.isdigit():
            return self.dict[int(input_value)]
        else:
            return self.dict[input_value]

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    S = MyClass()
    n, m = map(int, input().split())
    arr = [input().strip() for _ in range(n)]
    S.dict = {arr[i]: i+1 for i in range(n)}
    S.dict.update({i+1: arr[i] for i in range(n)})
    
    # Output
    for _ in range(m):
        print(S.sol(input().strip()))