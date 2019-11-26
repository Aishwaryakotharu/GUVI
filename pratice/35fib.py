n=int(input())
f1=0
f=1
f2=1
print(f1)
print(f2)
for i in range(1,n):
    f=f1+f2
    f1=f2
    f2=f
    print(f)