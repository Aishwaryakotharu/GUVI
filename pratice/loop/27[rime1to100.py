c=0
p=[]
for i in range(1,100):
    for j in range(2,i+1):
        if(i%j==0):
            break
        else:
            if i not in p:
                p.append(i)
print(p)
s=0
for i in range(0,len(p)):
    s=s+p[i]
print(s)