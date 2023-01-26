lines = [0]*31
input_lines = [int(input()) for _ in range(28)]
for i in range(28):
    lines[input_lines[i]] = 1
    
for i in range(1, 31):
    if lines[i] == 0:
        print(i)