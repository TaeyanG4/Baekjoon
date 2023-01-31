val = list(map(int,input().split()))

if val[0] <val [1] or ((val[0]-val[1])%2 != 0):
    print(-1)
else:
    a = (val[0]+val[1])/2
    b = val[0]-a
    print("%d %d" %(max(a,b),min(a,b)))
