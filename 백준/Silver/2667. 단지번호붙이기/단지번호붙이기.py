#import line
import sys
import heapq
import math
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(graph, n, y, x):
    
    q = deque()
    q.append((x, y))
    graph[y][x] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            ny, nx =  y + dy[k], x + dx[k]
            
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 1:
                q.append((nx, ny))
                graph[ny][nx] = 0
                cnt += 1
    return cnt

def solution(graph, n):
    res = list()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                res.append(bfs(graph, n, i, j))
    return res
                
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = int(input())
    graph = [[int(num) for num in input().strip()] for _ in range(n)]
    
    # output
    ans = solution(graph, n)
    ans.sort()
    print(len(ans))
    for i in ans:
        print(i)
