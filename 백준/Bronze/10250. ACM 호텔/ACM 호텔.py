import sys
input = sys.stdin.readline

def sol(h, w, n):
    assigned = 1
    for room in range(1, w + 1):
        for floor in range(1, h + 1):
            if assigned == n:
                return floor*100 + room
            assigned += 1

if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        h, w, n = map(int, input().split())
        print(sol(h, w, n))