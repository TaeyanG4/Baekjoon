for i in range(3):
    n = int(input())
    res = 0
    for j in range(n):
        res += int(input())
    if res == 0:
        print('0')
    elif res > 0:
        print('+')
    else:
        print('-')