m=int(input())
c=0
for i in range(1,m):
    if(m%i==0):
        c=c+1
if(c>1):
    print("not prime")
else:
    print("prime")
