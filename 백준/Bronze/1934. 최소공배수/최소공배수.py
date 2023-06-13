import math
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    g = math.gcd(a, b)
    print(a*b//g)