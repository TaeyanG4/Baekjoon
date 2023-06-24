n = int(input())
dic = {}
for i in range(n):
    name, val = input().split()
    if val == "enter":
        dic[name] = val
    else:
        del dic[name]
        
        
temp = sorted(dic.keys(), reverse=True)

for i in temp:
    print(i)