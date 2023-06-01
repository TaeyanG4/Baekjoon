a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
sec = 0
if a < 0:
    sec += abs(a*c) + d + (e*b)
elif a == 0:
    sec += d + (e*b)
else:
    sec += (b-a)*e
print(sec)