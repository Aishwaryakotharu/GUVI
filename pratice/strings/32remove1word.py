s=input().split()
x=input()
for i in range(0,len(s)):
    if(s[i]==x):
        a=s[i]
        print(a)
        s.pop(i)
        break
s=' '.join(map(str,s))
print(s)