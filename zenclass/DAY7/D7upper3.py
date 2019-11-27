a=input()
def isnewupper(a,i):
    for i in range(0,len(a)):
        x=1
        y=1
        for j in a:
            if(j>'A' and j<'Z'):
                x=x+1
            else:
                y=y+1
    if(x==len(a)):
        return True
    else:
        return False
                  

res=isnewupper(a)
print(res)