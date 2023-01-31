
## 전역 ##
minguck=list(map(int,input().split()))
manse=list(map(int,input().split()))
sum1=0
sum2=0

## 메인 ##
for i in range(0,len(minguck)):
    sum1+=minguck[i]
    sum2+=manse[i]

if sum1>sum2:
    print(sum1)
else : print(sum2)
