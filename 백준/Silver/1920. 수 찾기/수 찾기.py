import sys
input = sys.stdin.readline

def sol(n_arr, m_arr):
    v = []
    n_set = set(n_arr)
    for m in m_arr:
        if m in n_set:
            v.append(1)
        else:
            v.append(0)

    return '\n'.join(map(str, v))

if __name__ == '__main__':
    n_arr = [0]*int(input())
    n_arr = list(map(int, input().split()))
    m_arr = [0]*int(input())
    m_arr = list(map(int, input().split()))
    print(sol(n_arr, m_arr))