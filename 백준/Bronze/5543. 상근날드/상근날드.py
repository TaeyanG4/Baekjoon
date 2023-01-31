H=[0]*3
C=[0]*2
if __name__ == '__main__':
    for i in range(0, 3):
        H[i] = int(input())

    for i in range(0, 2):
        C[i] = int(input())

    H.sort()
    C.sort()
    print(H[0]+C[0]-50)
