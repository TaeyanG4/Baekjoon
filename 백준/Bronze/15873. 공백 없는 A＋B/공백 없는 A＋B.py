# import lines
#################################
import sys
#################################

def solution(n):
    p = 0
    n = list(n)
    ans = list()
    for _ in range(len(n)):
        a = n.pop()
        if a == '0':
            p += 1
        else:
            ans += [int(a) * (10 ** p)]
            p = 0
    return sum(ans)
    
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = input().strip()
    
    # output
    print(solution(n))
