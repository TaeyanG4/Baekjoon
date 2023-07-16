import sys
input = sys.stdin.readline

B = []
C = []
a = int(input())
for i in range(a):
    b,c = map(int, input().split())
    B.append(b)
    C.append(c)
print((max(B)-min(B))*(max(C)-min(C)))