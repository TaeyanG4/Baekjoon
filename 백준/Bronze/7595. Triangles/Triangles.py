while True:
    inp = int(input())
    if inp == 0:
        break
    for i in range(1, inp+1):
        for j in range(1, i+1):
            print("*", end="")
        print()