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
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __iter__(self):
        return iter((self.x, self.y))
    

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __iter__(self):
        return iter((self.p1, self.p2))


def ccw(p1, p2, p3):
    return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y)


def intersect(line1: Line, line2: Line) -> bool:
    A, B = line1
    C, D = line2
    if ccw(A, B, C) * ccw(A, B, D) < 0 and ccw(C, D, A) * ccw(C, D, B) < 0:
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
    x1, y1, x2, y2, x3, y3, x4, y4 = S()
    line1, line2 = Line(Point(x1, y1), Point(x2, y2)), Line(Point(x3, y3), Point(x4, y4))
    
    # output
    print(1 if intersect(line1, line2) else 0)
