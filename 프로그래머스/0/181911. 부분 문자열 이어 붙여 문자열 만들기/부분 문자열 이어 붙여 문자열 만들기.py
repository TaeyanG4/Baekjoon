def solution(my_strings, parts):
    answer = ''
    for s, p in zip(my_strings, parts):
        a, b = p[0], p[1]
        answer += s[a:b+1]
    return answer