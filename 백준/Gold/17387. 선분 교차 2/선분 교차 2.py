# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import time
# import pprint
# from collections import *
# from itertools import *
# from statistics import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

# https://johoonday.tistory.com/107
# https://hsdevelopment.tistory.com/390

class Point:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1, self.p2 = p1, p2
        
def ccw(p1: Point, p2: Point, p3: Point) -> int:
    temp = p1.x * p2.y + p2.x * p3.y + p3.x * p1.y
    temp -= p1.y * p2.x + p2.y * p3.x + p3.y * p1.x
    if temp > 0: 
        return 1
    elif temp < 0: 
        return -1
    else: 
        return 0


def isLined(p1: Point, p2: Point, p3: Point) -> bool:
    if p1.x < p2.x:
        return p2.x < p3.x
    elif p2.x < p1.x:
        return p3.x < p2.x
    else:
        if p1.y < p2.y:
            return p2.y < p3.y
        elif p2.y < p1.y:
            return p3.y < p2.y

def intersection(l1: Line, l2: Line) -> bool:
    ab = ccw(l1.p1, l1.p2, l2.p1) * ccw(l1.p1, l1.p2, l2.p2)
    cd = ccw(l2.p1, l2.p2, l1.p1) * ccw(l2.p1, l2.p2, l1.p2)
    
    if ab == 0 and cd == 0:
        if isLined(l1.p1, l1.p2, l2.p1) and isLined(l1.p1, l1.p2, l2.p2) or \
            isLined(l1.p2, l1.p1, l2.p1) and isLined(l1.p2, l1.p1, l2.p2):
                return False
        else:
            return True
    return ab <= 0 and cd <= 0

def solution(lines):
    if intersection(lines[0], lines[1]):
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    lines = []
    for _ in range(2):
        x1, y1, x2, y2 = map(int, input().split())
        lines.append(Line(Point(x1, y1), Point(x2, y2)))
    
    # output
    print(solution(lines))
