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

# 서 남 동 북
direction = ((0, 1), (1, 0), (0, -1), (-1, 0))

def turn(d, way):
    if way == 'L':
        return (d+3) % 4
    else:
        return (d+1) % 4

def sol(graph,apples,dic):
    
    # 사과 먹고싶다...
    for x, y in apples:
        graph[x-1][y-1] = 1
    
    # 뱀대가리
    snake_body = deque()
    snake_body.append((0,0))
    
    # 뱀 = 9
    x, y = 0, 0
    graph[x][y] = 9
    d = 0 
    play_time = 0
    
    while True:
        
        # # 디버깅용
        # print("-"*30)
        # print(f"{play_time}초")
        # for i in graph:
        #     print(i)
        # print("-"*30)
        
        play_time += 1
        x += direction[d][0]
        y += direction[d][1]
        
        # 벽에 부딪히면 종료
        if x < 0 or x >= n or y < 0 or y >= n:
            break

        if graph[x][y] == 1:
            graph[x][y] = 9
            snake_body.append((x,y))
            if play_time in dic:
                d = turn(d, dic[play_time])
                
        elif graph[x][y] == 0:
            graph[x][y] = 9
            snake_body.append((x,y))
            tx, ty = snake_body.popleft()
            graph[tx][ty] = 0
            if play_time in dic:
                d = turn(d, dic[play_time])
        
        else:
            break

    return play_time
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    # NxN board
    n = int(input())
    graph = [[0] * n for _ in range(int(n))]
    
    # apple count
    k = int(input())
    apples = [tuple(map(int, input().split())) for _ in range(k)]
    
    # direction count
    l = int(input())
    dic = dict()
    for _ in range(l):
        inp = input().split()
        dic.update({int(inp[0]): inp[1]})
        
    # Output
    print(sol(graph,apples,dic))
