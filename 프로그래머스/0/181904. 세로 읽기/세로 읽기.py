def solution(my_string, m, c):
    answer = ''
    for i in range(len(my_string)):
        if i%m+c == c:
            answer += my_string[i+c-1]
    return answer