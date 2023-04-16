try:
    while True:
        input_line = input()
        print(input_line)
except EOFError:
    exit(0)