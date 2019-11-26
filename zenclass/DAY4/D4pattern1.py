n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end='')
    print("")



n=int(input())
i=1
while(n>0):
    i=i+1
    print("*"*n)
    n=n-1