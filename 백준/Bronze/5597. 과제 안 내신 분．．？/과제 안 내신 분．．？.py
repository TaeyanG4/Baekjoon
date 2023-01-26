submitted = set(int(input()) for _ in range(28))
not_submitted = set(range(1, 31)) - submitted
not_submitted = sorted(list(not_submitted))
print(not_submitted[0])
print(not_submitted[1])