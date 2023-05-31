# import lines
import sys

def conquest(n, mat, i, j, size):
    if size == 1:
        return mat[i][j]
    
    half = size // 2
    lu = conquest(n, mat, i, j, half)
    ru = conquest(n, mat, i, j+half, half)
    ld = conquest(n, mat, i+half, j, half)
    rd = conquest(n, mat, i+half, j+half, half)
    
    if lu == ru == ld == rd == '0' or lu == ru == ld == rd == '1':
        return lu
    else:
        return '('+lu+ru+ld+rd+')'

def solution(n, mat):
    return conquest(n, mat, 0, 0, n)
    
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = int(input())
    mat = [list(map(str, input().strip())) for _ in range(n)] 
    
    # output
    print(solution(n, mat))