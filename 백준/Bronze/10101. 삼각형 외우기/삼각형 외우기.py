## 전역 ##
## 메인 ##
a=[0]*3
for i in range(0,3):
    a[i]=int(input())
if a[0]+a[1]+a[2]!=180 :
    print("Error")
elif a[0]==a[1]==a[2] :
    print("Equilateral")
elif a[0]==a[1] or a[1]==a[2] or a[2]==a[0] :
    print("Isosceles")
else :
    print("Scalene")
