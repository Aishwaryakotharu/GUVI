n=input()
s=0
for i in range(0,len(n)):
    if(n[i]>='0' and n[i]<='9'):
        
        s=s+int(n[i])
print(s)