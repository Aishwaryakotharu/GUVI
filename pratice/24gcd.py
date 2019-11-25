m=int(input())
n=int(input())
if(m<n):
    mi=m
else:
    mi=n
gcd=0
for i in range(1,mi+1):
    if(m%i==0 and n%i==0):
        if(i>gcd):
            gcd=i
print(gcd)
