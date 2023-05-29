#import line
import sys
import heapq
from collections import deque


def solution(n):
    heap_max, heap_min = list(), list()
    v = [False] * n
    for i in range(n):
        cmd, num = map(str, input().split())

        if cmd == 'I':
            heapq.heappush(heap_max, (-int(num), i))
            heapq.heappush(heap_min, (int(num), i))
            v[i] = True
        else:
            if num == '1':
                while heap_max and not v[heap_max[0][1]]:
                    heapq.heappop(heap_max)
                if heap_max:
                    v[heap_max[0][1]] = False
                    heapq.heappop(heap_max)
            
            else:
                while heap_min and not v[heap_min[0][1]]:
                    heapq.heappop(heap_min)
                if heap_min:
                    v[heap_min[0][1]] = False
                    heapq.heappop(heap_min)
    
    if True not in v:
        return 'EMPTY'
    else:
        while heap_max and v[heap_max[0][1]] == False:
            heapq.heappop(heap_max)
        while heap_min and v[heap_min[0][1]] == False:
            heapq.heappop(heap_min)
            
        return f"{-heap_max[0][0]} {heap_min[0][0]}"

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        # output
        print(solution(n))

