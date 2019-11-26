s=input()
l=[]
for i in range(len(s)-1,-1,-1):
    l.append(s[i])
x=''.join(map(str,l))
print(x)
