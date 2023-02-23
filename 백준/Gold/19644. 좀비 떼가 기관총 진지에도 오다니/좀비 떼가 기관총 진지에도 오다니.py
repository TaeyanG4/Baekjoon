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
    psum = [0] * (l+1) # psum = 누적합
    for i in range(1, l+1): # i = 좀비의 위치
        now = psum[i-1] - psum[max(0,i-ran)] # now = 현재 위치까지의 데미지
        if zombie[i] <= now + damage: # 좀비를 죽일 수 있으면
            psum[i] = psum[i-1] + damage # 누적합에 데미지 추가
        else: # 좀비를 죽일 수 없으면
            if boom: # 지뢰가 있으면
                boom -= 1 # 지뢰를 사용
                psum[i] = psum[i-1] # 누적합에 데미지 추가 안함
            else: # 지뢰가 없으면
                return "NO" # 실패
    return "YES" # 성공
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    l = int(input()) # l = 거리
    ran, damage = map(int, input().split())  # ran = 사정거리, damage = 데미지
    boom = int(input()) # boom = 지뢰수
    zombie = [0] + [int(input()) for _ in range(l)] # zombie = 좀비수
    
    # output
    print(sol(l, ran, damage, boom, zombie))