a="ABvD"
r=[]
def upper1(a):
    for i in range(0,len(a)):
        if(ord(a[i])>=96 and ord(a[i])<123):
            r.append("l")
        elif(ord(a[i])>64 and ord(a[i])<91):
            r.append("u")
    print(r)
    u=0
    l=0
    for i in range(0,len(r)):
        if (r[i]=='u'):
            u=u+1
        else:
            l=l+1
    print(u,l)
    if(u==len(r)):
        return True
    else:
        return False




res=upper1(a)
print(res)