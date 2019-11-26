n1=input()
n2=input()
if(len(n1)==len(n2)):
    x=len(n1)
else:
    print("cant be compared")
c=0
for i in range(0,x):
    if(n1[i]!=n2[i]):
        c=c+1
if(c>1):
    print("not equal")
else:
    print("no")
