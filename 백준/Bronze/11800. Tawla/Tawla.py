## taeyang's template (1.0.8)
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


def solution():
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(int(input())):
        a, b = S()
        if a < b:
            a, b = b, a
        if a == b:
            if a == 1:
                print(f"Case {i+1}: Habb Yakk")
            elif a == 2:
                print(f"Case {i+1}: Dobara")
            elif a == 3:
                print(f"Case {i+1}: Dousa")
            elif a == 4:
                print(f"Case {i+1}: Dorgy")
            elif a == 5:
                print(f"Case {i+1}: Dabash")
            elif a == 6:
                print(f"Case {i+1}: Dosh")
        elif a == 6 and b == 5:
            print(f"Case {i+1}: Sheesh Beesh")
        else:
            dic = {1: "Yakk", 2: "Doh", 3: "Seh", 4: "Ghar", 5: "Bang", 6: "Sheesh"}
            print(f"Case {i+1}: {dic[a]} {dic[b]}")
            