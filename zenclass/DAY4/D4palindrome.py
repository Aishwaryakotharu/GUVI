str=input()
a=0
j=len(str)-1
for i in range(0,len(str)):
    if(i<j):
        if(str[i]!=str[j]):
            a=1
            break
        j=j-1
if(a==1):
    print("np")
else:
    print("p")
