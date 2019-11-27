a=[10,20,30,40,50]   
n=1
for j in range(1,n+1):
    temp=a[0]
    for i in range(0,4):
        a[i]=a[i+1]
        l=len(a)-1
        a[l]=temp
    print(a)