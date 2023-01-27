while True:
    number = int(input())
    if number == 0:
        break
    number_str = str(number)
    if number_str == number_str[::-1]:
        print("yes")
    else:
        print("no")