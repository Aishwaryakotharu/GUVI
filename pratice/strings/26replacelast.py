s=input()
a=s.rfind(input())
x=input()
s=list(s)
s[a]=x
s=''.join(map(str,s))
print(s)