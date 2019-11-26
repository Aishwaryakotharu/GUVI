n=input()
x=input()
n=list(n)
c=0
for i in range(0,len(n)):
    if(n[i]==x):
        c=c+1
        print(i)
print("count :",c)        