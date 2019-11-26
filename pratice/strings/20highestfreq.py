n=input()
n=list(n)
c=1
a=[]
b=[]
for i in range(0,len(n)):
    x=n[i]
    for j in range(i+1,len(n)):
        if(x==n[j]):
            c=c+1
    if n[i] not in a:
        a.append(n[i])
        b.append(c)
    c=1
print(a)
print(b)


ma=b[0]
y=0
for i in range(1,len(b)):
    if(ma>b[i]):
        ma=ma
        i=i+1
        y=b[i]
        y
    else:
        ma=b[i]
        i=i+1
print(ma,y)