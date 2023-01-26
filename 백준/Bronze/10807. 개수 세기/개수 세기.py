v=[]

N=int(input())
v=input().split()
x=int(input())
count=0
for i in range(N):
    if int(v[i])==x:
        count+=1
print(count)