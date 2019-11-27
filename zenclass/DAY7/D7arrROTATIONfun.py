a=list(map(int,input().split()))  
n=int(input())
def rot(a,n):
    for j in range(1,n+1):
        temp=a[0]
    for i in range(0,4):
        a[i]=a[i+1]
        l=len(a)-1
    a[l]=temp
    print(a)
rot(a,n)