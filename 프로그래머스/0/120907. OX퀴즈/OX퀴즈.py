def solution(quiz):
    answer = []
    for v in quiz:
        a, b = v.split('=')
        answer.append("O" if eval(a) == int(b) else "X")
    return answer