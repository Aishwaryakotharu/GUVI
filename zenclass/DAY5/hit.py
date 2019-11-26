l=list(map(int,input().split()))
vl=[]
cl=[]
for i in range(0,len(l)):
    c=1
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            c=c+1
    vl.append(l[i])
    cl.append(c)
print(cl)
print(vl)

n=int(input())
d=[]
for i in range(0,len(cl)):
    if(cl[i]>1): 
        if vl[i] not in d:
            d.append(vl[i])
print(d[n-1])

