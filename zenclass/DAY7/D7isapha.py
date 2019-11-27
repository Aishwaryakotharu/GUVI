a=input()
def isalpa1(a):
    for i in range(0,len(a)):
        c=0
        for j in a:
            if(j>'A' and j<'z'):
                c=c+1
    if(c==len(a)):
        return True
    else:
        return False

x=isalpa1(a)
print(x)