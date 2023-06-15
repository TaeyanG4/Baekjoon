import sys

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
    
def solution():
    for _ in range(m):
        typ, a, b = map(int, input().split())
        if typ == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                print('YES')
            else:
                print('NO')

if __name__ == '__main__':
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)
    
    # input
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]

    # output
    solution()
