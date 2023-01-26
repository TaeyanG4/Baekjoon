n = int(input())
lines = list(set([input() for _ in range(n)]))
lines.sort()
lines.sort(key=len)
for line in lines:
    print(line)