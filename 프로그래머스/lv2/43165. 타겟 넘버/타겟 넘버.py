answer = 0

def dfs(stack, count, numbers, target):
    global answer

    if len(numbers) == count:
        if sum(stack) == target:
            answer += 1
            return
        return
    
    stack.append(0 + numbers[count])
    dfs(stack, count+1, numbers, target)
    stack.pop()

    stack.append(0 - numbers[count])
    dfs(stack, count+1, numbers, target)
    stack.pop()

def solution(numbers, target):
    stack = list()
    dfs(stack, 0, numbers, target)
    return answer