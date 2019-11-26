n=input()
n=list(n)
c=1
a=[]
for i in range(0,len(n)):
    x=n[i]
    for j in range(i+1,len(n)):
        if(x==n[j]):
            c=c+1
    if n[i] not in a:
        a.append(n[i])
        a.append(c)
    c=1
print(a)