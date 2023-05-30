#import line
import sys
import heapq
import math
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(graph, y, x, n, m):
    q = deque([(y, x)])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if (0 <= ny < n) and (0 <= nx < m): 
                if graph[ny][nx] == 1:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append((ny, nx))
    
    return graph[n-1][m-1]

def solution(n, m, graph):
    return bfs(graph, 0, 0, n, m)
                
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n, m = map(int, input().split())
    graph = [[int(char) for char in input().strip()] for _ in range(n)]
    
    # output
    print(solution(n, m, graph))
