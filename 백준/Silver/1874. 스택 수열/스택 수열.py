n = int(input())
seq = [int(input()) for _ in range(n)]

stack = []
result = []

for i in range(1, n+1):
    stack.append(i)
    result.append("+")
    while stack and stack[-1] == seq[0]:
        stack.pop()
        result.append("-")
        seq.pop(0)

if seq:
    print("NO")
else:
    for op in result:
        print(op)