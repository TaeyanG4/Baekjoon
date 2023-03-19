def solution(n):
    for num in range(1, n+1):
        s = input()
        print(str(num)+". "+s)

if __name__ == '__main__':
    # input = sys.stdin.readline
    
    # input
    n = int(input())

    # output
    solution(n)