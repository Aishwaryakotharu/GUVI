a=list(map(int,input().split()))
s=list(map(int,input().split()))
n=int(input())

for j in range(1,n+1):
    temp=a[0]
    for i in range(0,len(a)-1):
        a[i]=a[i+1]
        l=len(a)-1
    a[l]=temp
    print(a,s)
    if(a==s):
        print(j)
        break