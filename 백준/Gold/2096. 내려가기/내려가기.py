# import lines
#################################
import sys

def solution(max_li, min_li):
    for i in range(n):
        a1, a2, a3 = map(int, input().split())
        for j in range(3):
            if j == 0:
                max_temp[j] = a1 + max(max_li[j], max_li[j+1])
                min_temp[j] = a1 + min(min_li[j], min_li[j+1])
            elif j == 1:
                max_temp[j] = a2 + max(max_li[j-1], max_li[j], max_li[j+1])
                min_temp[j] = a2 + min(min_li[j-1], min_li[j], min_li[j+1])
            else:
                max_temp[j] = a3 + max(max_li[j-1], max_li[j])
                min_temp[j] = a3 + min(min_li[j-1], min_li[j])
        
        for j in range(3):
            max_li[j] = max_temp[j]
            min_li[j] = min_temp[j]
    
    return max(max_li), min(min_li)

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = int(input())
    max_li = [0] * 3
    min_li = [0] * 3
    max_temp = [0] * 3
    min_temp = [0] * 3 
            
    # output
    print(*solution(max_li, min_li))
