def solution(my_string):
    answer = []
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        answer.append(my_string.count(c))
    return answer