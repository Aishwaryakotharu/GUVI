m=int(input())
n=int(input())
if(m>n):
    ma=m
else:
    ma=n
lcf=1
a=[]
for i in range(1,10):
    for j in range(1,10):
        if(m*i == n*j):
            lcf=m*i
            a.append(lcf)

           
print(a[0])