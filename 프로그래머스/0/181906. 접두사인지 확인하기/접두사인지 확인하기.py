def solution(my_string, is_prefix):
    answer = 0
    for i in range(1, len(my_string)+1):
        if is_prefix == my_string[:i]:
            answer = 1
    return answer