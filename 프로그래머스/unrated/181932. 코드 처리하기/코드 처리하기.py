def solution(code):
    answer = ''
    mode = 0
    for i, c in enumerate(code):
        if mode == 0:
            if c != '1' and i % 2 == 0:
                answer += c
            elif c == '1':
                mode = 1
        elif mode == 1:
            if c != '1' and i % 2 == 1:
                answer += c
            elif c == '1':
                mode = 0
        
    if answer == '':
        return "EMPTY"
    else:
        return answer