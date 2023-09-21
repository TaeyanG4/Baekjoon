## taeyang's template (1.0.7)
# https://yiyj1030.tistory.com/508
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
    
    def __iter__(self):
        return iter((self.x, self.y))


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1, self.p2 = p1, p2
        
    def __iter__(self):
        return iter((self.p1, self.p2))


# p1, p2, p3가 반시계 방향이면 양수, 시계 방향이면 음수, 일직선이면 0
def ccw(p1: Point, p2: Point, p3: Point) -> int:
    return ((p2.x - p1.x) * (p3.y - p1.y)) - ((p2.y - p1.y) * (p3.x - p1.x))


def intersect(line1: Line, line2: Line) -> bool:
    
    A, B = line1
    C, D = line2
    
    ccwABC = ccw(A, B, C)
    ccwABD = ccw(A, B, D)
    ccwCDA = ccw(C, D, A)
    ccwCDB = ccw(C, D, B)
    
    mx1, my1,  = min(A.x, B.x), min(A.y, B.y)
    mx2, my2,  = max(A.x, B.x), max(A.y, B.y)
    mx3, my3,  = min(C.x, D.x), min(C.y, D.y)
    mx4, my4,  = max(C.x, D.x), max(C.y, D.y)
    
    # for debugging
    # print(ccwABC, ccwABD, ccwCDA, ccwCDB)
    # print(mx1, my1, mx2, my2, mx3, my3, mx4, my4)
    
    # 평행하는 경우
    if ccwABC * ccwABD == 0 and ccwCDA * ccwCDB == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4  and my3 <= my2:
            return True
    
    # 교차하는 경우
    else:
        if ccwABC * ccwABD <= 0 and ccwCDA * ccwCDB <= 0:
            return True
    
    return False


# 기울기 비교 함수
def slope_comparison(line1, line2):
    """
        기울기1 = x2-x1 / y2-y1
        기울기2 = x4-x3 / y4-y3
        x2-x1 / y2-y1 = x4-x3 / y4-y3
        (y2-y1)*(x4-x3)=(y4-y3)*(x2-x1)
    """
    p1, p2 = line1
    p3, p4 = line2
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    if (x4 - x3) * (y2 - y1) == (x2 - x1) * (y4 - y3):
        return True
    else:
        return False
    

def get_intersect_point(line1: Line, line2: Line) -> Point:
    
    A, B = line1
    C, D = line2
    A, B, C, D = tuple(A), tuple(B), tuple(C), tuple(D)
    
    if slope_comparison(line1, line2): # 기울기 비교
        if max(x1, x2) == min(x3, x4) or max(x3, x4) == min(x1, x2): # 한 점일 경우
            if A in [C, D]:
                print(*A)
            elif B in [C, D]:
                print(*B)
    else:
        A, B = line1
        C, D = line2
        
        # 두 직선의 방정식
        a1 = B.y - A.y
        b1 = A.x - B.x
        c1 = a1 * A.x + b1 * A.y
        
        a2 = D.y - C.y
        b2 = C.x - D.x
        c2 = a2 * C.x + b2 * C.y
        
        # Cramer의 규칙 (행렬식); 0이면 평행, 아니면 교차
        determinant = a1 * b2 - a2 * b1
        if determinant == 0:
            return None
        else:
            x = (b2 * c1 - b1 * c2) / determinant
            y = (a1 * c2 - a2 * c1) / determinant
            return x, y


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
        p = get_intersect_point(line1, line2)
        if p is not None:
            print(*p)
    else:
        print(0)