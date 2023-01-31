A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

val1 = (A[3]*3600+A[4]*60+A[5])-(A[0]*3600+A[1]*60+A[2])
val2 = (B[3]*3600+B[4]*60+B[5])-(B[0]*3600+B[1]*60+B[2])
val3 = (C[3]*3600+C[4]*60+C[5])-(C[0]*3600+C[1]*60+C[2])

print(val1//3600,(val1%3600)//60,(val1%3600)%60)
print(val2//3600,(val2%3600)//60,(val2%3600)%60)
print(val3//3600,(val3%3600)//60,(val3%3600)%60)
