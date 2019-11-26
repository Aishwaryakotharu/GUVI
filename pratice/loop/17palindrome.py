n=int(input())
t=n
s=0
while(n>0):
    a=n%10
    s=(s*10)+a
    n=n//10

if(s==t):
    print("p")
else:
    print("np")