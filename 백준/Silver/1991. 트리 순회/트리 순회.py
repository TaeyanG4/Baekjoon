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

def pre_order(root):
    if root != '.':
        print(root, end='')
        pre_order(tree[root][0])
        pre_order(tree[root][1])

def in_order(root):
    if root != '.':
        in_order(tree[root][0])
        print(root, end='')
        in_order(tree[root][1])

def post_order(root):
    if root != '.':
        post_order(tree[root][0])
        post_order(tree[root][1])
        print(root, end='')

def solution():
    pre_order('A')
    print()
    in_order('A')
    print()
    post_order('A')

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = int(input())
    tree = {}
    for _ in range(n):
        root, left, right = input().split()
        tree[root] = [left, right]
    
    # output
    solution()
    