#import line
import sys
import heapq
from collections import deque

def solution(n, k):
    dist = [0] * 100001
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            return dist[x]
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                q.append(nx)
    
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n, k = map(int, input().split())
    
    # output
    print(solution(n, k))

