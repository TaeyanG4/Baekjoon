s = input().strip()
b, c = 0, 0
for i in s:
    if i == 'B':
        b += 1
    else:
        c += 1
print((b//2)+(c//2))