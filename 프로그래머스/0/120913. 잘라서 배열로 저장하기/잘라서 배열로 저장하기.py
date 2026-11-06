def solution(my_str, n):
    answer = []
    i = 0
    while True:
        if i >= len(my_str):
            break
        answer.append(my_str[i:i+n])
        i += n
    return answer