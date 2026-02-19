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
# getcontext().prec = 20
#################################

# 물병자리	1월 20일 ~ 2월 18일
# 물고기자리	2월 19일 ~ 3월 20일
# 양자리	3월 21일 ~ 4월 19일
# 황소자리	4월 20일 ~ 5월 20일
# 쌍둥이자리	5월 21일 ~ 6월 21일
# 게자리	6월 22일 ~ 7월 22일
# 사자자리	7월 23일 ~ 8월 22일
# 처녀자리	8월 23일 ~ 9월 22일
# 천칭자리	9월 23일 ~ 10월 22일
# 전갈자리	10월 23일 ~ 11월 22일
# 사수자리	11월 23일 ~ 12월 21일
# 염소자리	12월 22일 ~ 1월 19일

def solution(mm, dd):
    if mm == 3 and dd >= 21:
        return "Aries"
    elif mm == 4 and dd <= 19:
        return "Aries"
    elif mm == 4 and dd >= 20:
        return "Taurus"
    elif mm == 5 and dd <= 20:
        return "Taurus"
    elif mm == 5 and dd >= 21:
        return "Gemini"
    elif mm == 6 and dd <= 21:
        return "Gemini"
    elif mm == 6 and dd >= 22:
        return "Cancer"
    elif mm == 7 and dd <= 22:
        return "Cancer"
    elif mm == 7 and dd >= 23:
        return "Leo"
    elif mm == 8 and dd <= 22:
        return "Leo"
    elif mm == 8 and dd >= 23:
        return "Virgo"
    elif mm == 9 and dd <= 22:
        return "Virgo"
    elif mm == 9 and dd >= 23:
        return "Libra"
    elif mm == 10 and dd <= 22:
        return "Libra"
    elif mm == 10 and dd >= 23:
        return "Scorpio"
    elif mm == 11 and dd <= 22:
        return "Scorpio"
    elif mm == 11 and dd >= 23:
        return "Sagittarius"
    elif mm == 12 and dd <= 21:
        return "Sagittarius"
    elif mm == 12 and dd >= 22:
        return "Capricorn"
    elif mm == 1 and dd <= 19:
        return "Capricorn"
    elif mm == 1 and dd >= 20:
        return "Aquarius"
    elif mm == 2 and dd <= 18:
        return "Aquarius"
    elif mm == 2 and dd >= 19:
        return "Pisces"
    elif mm == 3 and dd <= 20:
        return "Pisces"


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    idol = set()
    for i in range(7):
        mm, dd = S()
        idol.add(solution(mm, dd))
        
    n = int(input())
    candidate = []
    for i in range(n):
        mm, dd = S()
        candidate.append((solution(mm, dd), (mm, dd)))
    
    ans = []
    cnt = 0
    for c in candidate:
        if c[0] not in idol:
            ans.append((c[1][0], c[1][1]))
            cnt += 1
    ans.sort(key=lambda x: (x[0], x[1]))
    
    if cnt == 0:
        print("ALL FAILED")
    else:
        for a in ans:
            print(a[0], a[1])
