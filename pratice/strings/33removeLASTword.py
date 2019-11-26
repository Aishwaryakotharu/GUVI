s=input().split()
x=input()
for i in range(len(s)-1,-1,-1):
    if(s[i]==x):
        a=s[i]
        print(a)
        s.pop(i)
        break
s=' '.join(map(str,s))
print(s)