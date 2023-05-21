n,a,b=map(int,input().split())
if a-n==b-n:
    print("Anything")
elif a-n<b-n:
    print("Bus")
else:
    print("Subway")