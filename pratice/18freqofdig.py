n=int(input())
l=[]
while(n>0):
    a=n%10
    l.append(a)
    n=n//10
c=0
vl=[]
cl=[]


for i in range(0,len(l)):
    c=1
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            c=c+1
    vl.append(l[i])
    cl.append(c)

print(vl,cl)
