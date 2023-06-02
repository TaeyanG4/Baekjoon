num, baseNum = map(int, input().split())
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
baseVal = ""
while num:
    num, i = divmod(num, baseNum)
    baseVal = alphabet[i] + baseVal
print(baseVal)