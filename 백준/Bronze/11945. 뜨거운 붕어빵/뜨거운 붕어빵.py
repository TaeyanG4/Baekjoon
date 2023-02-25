x, y = map(int, input().split())
li = [input() for _ in range(x)]
for i in li:
    print(i[::-1])