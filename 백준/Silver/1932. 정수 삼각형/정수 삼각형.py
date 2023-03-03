def solution(n, li):
    for i in range(1, n):
        for j in range(len(li[i])):
            if j == 0:
                li[i][j] += li[i-1][j] 
            elif j == i:
                li[i][j] += li[i-1][j-1]
            else:
                li[i][j] += max(li[i-1][j-1], li[i-1][j])
    return max(li[n-1])
    
if __name__ == '__main__':
    
    # input
    li = list()
    n = int(input())
    for i in range(n):
        li.append(list(map(int, input().split())))

    # output
    print(solution(n, li))