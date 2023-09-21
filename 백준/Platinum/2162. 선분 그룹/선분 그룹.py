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
from collections import *
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


def ccw_direction(p1: Point, p2: Point, p3: Point) -> int:
    dx1, dy1 = p2.x - p1.x, p2.y - p1.y
    dx2, dy2 = p3.x - p1.x, p3.y - p1.y
    
    if dx1 * dy2 > dy1 * dx2:
        return 1
    elif dx1 * dy2 < dy1 * dx2:
        return -1
    else:
        if dx1 == 0 and dy1 == 0:
            return 0
        elif (dx1 * dx2 < 0) or (dy1 * dy2 < 0):
            return -1
        elif (dx1 * dx1 + dy1 * dy1) < (dx2 * dx2 + dy2 * dy2):
            return 1
        else:
            return 0


def intersect(line1: Line, line2: Line) -> bool:
    A, B = line1
    C, D = line2
    if ccw_direction(A, B, C) * ccw_direction(A, B, D) <= 0 and ccw_direction(C, D, A) * ccw_direction(C, D, B) <= 0:
        return True
    else:
        return False


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


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
    n = int(input())
    lines = []
    parent = [i for i in range(n)]
    for _ in range(n):
        x1, y1, x2, y2 = S()
        lines.append(Line(Point(x1, y1), Point(x2, y2)))
        
    
    for i in range(n):
        for j in range(i+1, n):
            if intersect(lines[i], lines[j]):
                union(i, j)
                
    parent = [find(i) for i in parent]
        
    # output
    cnt = Counter(parent)
    print(len(cnt))
    print(max(cnt.values()))
