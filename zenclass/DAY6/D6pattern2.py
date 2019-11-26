l=list(map(int,input().split()))
i=0
for i in range(0,len(l)):
    if(i%2==0):
        x=l[i]
        for k in range(0,x):
            print("*",end='')
        
    else:
        x=l[i]
        for k in range(0,x):
            print("+",end='')
    print("")
    
