n=input()
x=n.split()
a=[]
for i in range(len(x)-1,-1,-1):
    a.append(x[i])
print(a)