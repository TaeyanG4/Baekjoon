def solution(arr, delete_list):
    for i in set(delete_list):
        if i in arr:
            arr.remove(i)
    return arr