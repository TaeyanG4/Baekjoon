import sys
input = sys.stdin.readline

def sol(v):
    cnt = v // 2 
    while True:
        if v == cnt + sum(map(int, str(cnt))): 
            return cnt
        cnt += 1
        if cnt > v: 
            return 0

if __name__ == '__main__':
        print(sol(int(input())))