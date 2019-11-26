l1=list(map(str,input().split()))
l2=list(map(str,input().split()))
l3=list(map(str,input().split()))
for i in range(0,len(l1)):
    if(l2[i]=="M"):
        a="Mr"+l1[i]
        l1[i]=a
    elif(l2[i]=="F"):
        if(l3[i]=="M"):
            a="MRs"+l1[i]
            l1[i]=a
        else:
            a="Ms"+l1[i]
            l1[i]=a
    else:
        break
print(l1)