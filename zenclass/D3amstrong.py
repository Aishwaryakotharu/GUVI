a=input()
s=0
c=0
l=len(a)
a=int(a)
y=a
for i in range(0,l):
    x=a%10
    c=x**l
    a=a//10
    s=s+c
    

if(s==y):
    print("yes")
else:
    print("no")
