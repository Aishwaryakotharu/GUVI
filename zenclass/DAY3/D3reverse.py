r=0
n=int(input())
while(n>0):
    a=n%10
    r=(r*10)+a
    n=n//10
print(r)
