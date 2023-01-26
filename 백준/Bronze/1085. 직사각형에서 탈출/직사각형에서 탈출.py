x, y, w, h = map(int, input().split())
v = []
v.append(x)
v.append(y)
v.append(w-x)
v.append(h-y)
print(min(v))