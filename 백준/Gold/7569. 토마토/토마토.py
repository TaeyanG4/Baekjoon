#import line
import sys
from collections import deque

dh = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]


def bfs(q):
    while q:
        k, x, y = q.popleft()
        for i in range(6):
            nk, nx, ny = k+dh[i], x+dx[i], y+dy[i]
            if 0 <= nk < h and 0 <= nx < n and 0 <= ny < m and  li[nk][nx][ny] == 0:
                li[nk][nx][ny] = li[k][x][y] + 1
                q.append((nk, nx, ny))

def solution():
    pass

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    m, n, h = map(int, input().split())
    li = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)] 
    
    q = deque([])
    res = 0
    
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if li[k][i][j] == 1:
                    q.append((k, i, j))
    
    bfs(q)
    for h in li:
        for i in h:
            for j in i:
                if j == 0:
                    print(-1)
                    exit(0)
            res = max(res, max(i))
        
    # output
    print(res-1)

