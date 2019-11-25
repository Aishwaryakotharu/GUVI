l=list(map(int,input().split()))
count=[]
c=1
cl=[]
vl=[]


for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if (l[i] == l[j]):
            c=c+1
    cl.append(c)  
    vl.append(l[i])
    c=1
    
print(l)
print(cl)   
print(vl)
