n=input()
n=list(n)
c=0
s=['a','e','i','o','u']
for i in range(0,len(n)):
    if n[i] in s:
        c+=1
if(c>1):
    print("yes")
else:
    print("no")