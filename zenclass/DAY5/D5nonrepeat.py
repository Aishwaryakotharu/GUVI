l=list(map(int,input().split()))
c=1
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)-1):
        if (l[i] == l[j]):
            c=c+1
            break

    if(c>1):
        break
print(l[i],c)
    