n=input()
n=list(n)
for i in range(0,len(n)):
    if(ord(n[i])>96 and ord(n[i])<123):
        n[i]=n[i].upper()
    else:
        n[i]=n[i].lower()
a=''.join(map(str,n))
print(a)