def solution(num_list):
    answer = 1
    for i in num_list:
        answer *= i
    return 1 if answer < sum(num_list)**2 else 0