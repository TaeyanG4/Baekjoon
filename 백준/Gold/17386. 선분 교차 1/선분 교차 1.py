## taeyang's template (1.0.7)
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

class Point:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        
class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1, self.p2 = p1, p2
        
# p1, p2, p3가 반시계 방향이면 양수, 시계 방향이면 음수, 일직선이면 0
def ccw(p1: Point, p2: Point, p3: Point) -> int:
    return ((p2.x - p1.x) * (p3.y - p1.y)) - ((p2.y - p1.y) * (p3.x - p1.x))

def intersect(line1: Line, line2: Line) -> bool:
    A, B, C, D = line1.p1, line1.p2, line2.p1, line2.p2
    ab, cd = ccw(A, B, C) * ccw(A, B, D), ccw(C, D, A) * ccw(C, D, B)
    if ab == 0 and cd == 0:
        if B < A: 
            A, B = B, A
        if D < C: 
            C, D = D, C
        return C <= B and A <= D
    return ab <= 0 and cd <= 0

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    # n, m = map(int, input().split())
    # lst = [*map(int, input().split())]
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    line1 = Line(Point(x1, y1), Point(x2, y2))
    line2 = Line(Point(x3, y3), Point(x4, y4))
    
    # output
    if intersect(line1, line2):
        print(1)
    else:
        print(0)
