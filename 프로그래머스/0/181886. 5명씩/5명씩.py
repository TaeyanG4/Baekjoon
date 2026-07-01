def solution(names):
    ans = []
    for i, v in enumerate(names):
        if i % 5 == 0:
            ans.append(v)
    return ans