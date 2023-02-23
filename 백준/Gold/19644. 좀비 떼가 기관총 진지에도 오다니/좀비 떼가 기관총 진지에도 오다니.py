# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import json
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def sol(l, ran, damage, boom, zombie):
    dq = deque()
    psum = [0] * (l+1)
    
    for i in range(1, l+1):
        now = psum[i-1] - psum[max(0,i-ran)]
        if zombie[i] <= now + damage:
            psum[i] = psum[i-1] + damage
        else:
            if boom:
                boom -= 1
                psum[i] = psum[i-1]
            else:
                return "NO"
    return "YES"
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    l = int(input()) # l = 거리
    ran, damage = map(int, input().split())  # ran = 사정거리, damage = 데미지
    boom = int(input()) # boom = 지뢰수
    zombie = [0] + [int(input()) for _ in range(l)] # zombie = 좀비수
    
    # output
    print(sol(l, ran, damage, boom, zombie))