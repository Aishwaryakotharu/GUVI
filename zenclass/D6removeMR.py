l1=list(map(str,input().split()))

f"""or i in range(0,len(l1)):
    s=l1[i]
    for j in range(0,len(s)):
        if(s[j]=="."):
            a=j+1
            l1[i]=s[a:]
print(l1)"""


for i in range(len(l1)):
    pos=l1[i].index('.')
    str=l1[i]
    l1[i]=str[pos+1:]
print(l1)