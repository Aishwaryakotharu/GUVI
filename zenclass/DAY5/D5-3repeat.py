l=list(map(int,input().split()))
cl=[]
vl=[]
c=1
for i in range(0,len(l)):
    c=1
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            c=c+1
    vl.append(l[i])
    cl.append(c)
    
print(vl)
print(cl)
p=0
d=[]
for i in range(0,len(cl)):
    if(cl[i]>1):
        if vl[i] not in d:
            d.append(vl[i])
print(d)
print(d[2])
        
