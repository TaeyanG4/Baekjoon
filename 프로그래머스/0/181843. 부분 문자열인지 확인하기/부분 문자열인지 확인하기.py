def solution(my_string, target):
    cnt = len(my_string) - len(target)
    for i in range(cnt+1):
        if my_string[i:i+len(target)] == target:
            return 1
    else:
        return 0