l=list(map(int,input().split()))
count=[]
c=1
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if (l[i] == l[j]):
            c=c+1
            
    if(c>1):
        break
print(l[i],c)
    