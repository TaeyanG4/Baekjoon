def solution(num_list):
    answer = 0
    for i in num_list:
        val = i
        while True:
            if val <= 1:
                break
            if val % 2 == 1:
                val -= 1
            val //= 2
            answer += 1
    return answer