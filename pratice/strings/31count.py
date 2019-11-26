s=input().split()
x=input()
c=1
for i in range(0,len(s)):
    if(s[i]==x):
        c=c+1
        print(i)
        
print(c)