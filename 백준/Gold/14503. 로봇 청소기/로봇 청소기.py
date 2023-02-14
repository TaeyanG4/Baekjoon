# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def sol(n, m, r, c, d):
    room = [list(map(int, input().split())) for _ in range(n)]
    clean_cnt = 0
    
    while True:
        # 0 = 청소해야함 1 = 벽, 2 = 청소완료
        # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        
        # 디버깅용
        if room[r][c] == 0:
            if d == 0:
                room[r][c] = 'A'
            elif d == 1:
                room[r][c] = '>'
            elif d == 2:
                room[r][c] = 'V'
            elif d == 3:
                room[r][c] = '<'
            clean_cnt += 1
        
            
        marker = False # 청소할 칸이 있는지 확인하는 변수
        for i in range(4):
            if room[r + dx[i]][c + dy[i]] == 0:
                marker = True
                
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        if marker is True:

            #왼쪽으로 회전한다.
            d = (d+3) % 4
            for _ in range(4):
                # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
                if room[r + dx[d]][c + dy[d]] == 0:
                    r += dx[d]
                    c += dy[d]
                    break
                else:
                    d = (d+3) % 4 # 없으면 왼쪽으로 회전
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        elif marker is False:
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            if room[r + dx[(d+2) % 4]][c + dy[(d+2) % 4]] == 1:
                return clean_cnt
                    
            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            if room[r + dx[(d+2) % 4]][c + dy[(d+2) % 4]] != 1:
                r += dx[(d+2) % 4]
                c += dy[(d+2) % 4]
            
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    
    # Output
    print(sol(n, m, r, c, d))