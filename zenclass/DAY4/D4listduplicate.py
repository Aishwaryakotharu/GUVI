l1=input().split()
l2=[0]*len(l1)
l3=[]


for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if(l1[i]==l1[j]):
            l2[i]+=1
        
for i in range(0,len(l2)):
    if(l2[i]==0):
        l3.append(l1[i])
print(l3)