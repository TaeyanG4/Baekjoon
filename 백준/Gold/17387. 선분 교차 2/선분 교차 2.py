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
    
    # self.x, self.y를 반환 (x, y = point1)
    def __iter__(self):
        return iter((self.x, self.y))
        
class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1, self.p2 = p1, p2
    
    # self.p1, self.p2를 반환 (p1, p2 = line1)
    def __iter__(self):
        return iter((self.p1, self.p2))


def ccw(p1: Point, p2: Point, p3: Point) -> int:
    
    # 벡터의 외적을 이용한 방법
    # 두 벡터의 외적을 구하면 두 벡터가 이루는 사각형의 넓이가 나온다.
    dx1, dy1 = p2.x - p1.x, p2.y - p1.y # p1 -> p2
    dx2, dy2 = p3.x - p1.x, p3.y - p1.y # p1 -> p3
    
    # ((p2.x - p1.x) * (p3.y - p1.y)) - ((p2.y - p1.y) * (p3.x - p1.x))과 본질은 비슷하다 '-'자리에 >, <, =를 넣어서 방향을 구한다.
    if dx1 * dy2 > dy1 * dx2:
        return 1
    elif dx1 * dy2 < dy1 * dx2:
        return -1
    else:
        # p1와 p2가 같은 위치에 있을 경우 (점)
        if dx1 == 0 and dy1 == 0:
            return 0
        # p1을 기준으로 p2와 p3가 서로 반대 방향에 있을 경우 예) p2 <-> p1 <-> p3
        elif (dx1 * dx2 < 0) or (dy1 * dy2 < 0):
            return -1
        # p1에서 p3까지의 거리가 p1에서 p2까지의 거리보다 길다면 1을 반환 p1 <-> p2 -/- p3
        elif (dx1 * dx1 + dy1 * dy1) < (dx2 * dx2 + dy2 * dy2):
            return 1
        else:
            return 0


def intersect(line1: Line, line2: Line) -> bool:
    A, B = line1
    C, D = line2
    if ccw(A, B, C) * ccw(A, B, D) <= 0 and ccw(C, D, A) * ccw(C, D, B) <= 0:
        return True
    else:
        return False


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