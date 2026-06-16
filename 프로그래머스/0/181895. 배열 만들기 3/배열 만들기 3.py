def solution(arr, intervals):
    answer = []
    a_arr, b_arr = intervals
    answer.extend(arr[a_arr[0]:a_arr[1]+1])
    answer.extend(arr[b_arr[0]:b_arr[1]+1])
    return answer