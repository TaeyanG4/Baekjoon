def solution(numbers):
    ans = [0,1,2,3,4,5,6,7,8,9]
    for num in numbers:
        ans[num] = 0
    return sum(ans)