li = list(map(int, input().split()))
li.sort()
ans = (li[0]+li[3])-(li[1]+li[2])
print(abs(ans))