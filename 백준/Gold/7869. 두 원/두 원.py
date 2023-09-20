## taeyang's template (1.0.7)
# https://wondangcom.com/1900
#################################
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
# from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################

def dist(p1, p2):
    return ((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2) ** 0.5

def solution():
    """
        # cosA = (b2+c2-a2)/2bc 이므로 cos(theta/2) = (r1^2 + d^2 - r2^2) / (2 * r1 * d)
        # theta = 2 * acos((r1^2 + d^2 - r2^2) / (2 * r1 * d)) # acos는 역코사인(cos^−1)을 뜻한다
        
        # S(부채꼴의 넓이) = (r^2 * theta) / 2
        # Stri(부채꼴 안의 삼각형의 넓이) = (r^2 * sin(theta)) / 2
    """
    
    # 원이 겹치지 않는 경우
    if d >= r1+r2:
        return 0
    # 원이 다른 원을 포함하는 경우
    elif d <= abs(r1-r2): 
        return PI * min(r1, r2) ** 2
    # 원이 겹치는 경우
    else:
        
        # 코사인 법칙
        theta1 = 2 * math.acos((r1**2 + d**2 - r2**2) / (2 * r1 * d))
        theta2 = 2 * math.acos((r2**2 + d**2 - r1**2) / (2 * r2 * d))
        
        # 부채꼴의 넓이
        s1 = ((r1**2 * theta1) - (r1**2 * math.sin(theta1))) / 2
        s2 = ((r2**2 * theta2) - (r2**2 * math.sin(theta2))) / 2
        
        return s1 + s2
    
if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    d = dist((x1, y1), (x2, y2))
    PI = math.pi

    # output
    print(f'{solution():.3f}')