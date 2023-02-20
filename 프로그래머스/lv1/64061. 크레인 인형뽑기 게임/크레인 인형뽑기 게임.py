def solution(board, moves):
    stack = list()
    answer = 0
    
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                stack.append(b[m-1])
                b[m-1] = 0
                break
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    return answer