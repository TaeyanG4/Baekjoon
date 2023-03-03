def solution(triangle):
    li = triangle
    for i in range(1, len(li)):
        for j in range(len(li[i])):
            if j == 0:
                li[i][j] += li[i-1][j] 
            elif j == i:
                li[i][j] += li[i-1][j-1]
            else:
                li[i][j] += max(li[i-1][j-1], li[i-1][j])
    return max(li[len(li)-1])