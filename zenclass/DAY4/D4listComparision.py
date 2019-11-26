l1=[1,2,3,4,5]
l2=[2,3,4,6,8]
for (i,j) in zip(l1,l2):
    if(i!=j):
        count=1
if(count==1):
    print("different")
else:
    print("same")



l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=len(l1)
s=0
for i in range(0,l):
    if(l1[i]!=l2[i]):
        i=i+1
        s=s+1
print(s)
if(s>0):
    print("d")
else:
    print("s")

