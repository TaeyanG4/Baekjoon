import sys
input = sys.stdin.readline

def sol(v):
    for i in range(len(str(v))*9, 0, -1):
        dis = abs(v-i)
        if v==dis+sum(map(int, str(dis))):
            return dis
    return 0

if __name__ == '__main__':
        print(sol(int(input())))