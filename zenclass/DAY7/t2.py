
n=int(input())
l=list(map(int,input().split()))

cl=[]
vl=[]
for i in range(0,n):
    c=1
    for j in range(i+1,n):
        if(l[i]==l[j]):
            c=c+1
    cl.append(c)
    vl.append(l[i])
x={}
for i in range(0,len(cl)):
    if vl[i] not in x:
        x[vl[i]]=cl[i]

print(x)
f=1
for i in x:
    
    if(x[i]==1):
        f=f+1
        
        if(f>3):
            print(i)
            break
        
print(f)