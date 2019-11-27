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
x={}
for i in range(0,len(vl)):
    if l[i] not in x:
        x[vl[i]]=cl[i]
print(x)

f=1
e=0
for i in x:
    if(x[i]==1):
        f=f+1
        if(f>3):
            print(i)