n=input()
n=list(n)
c1=0
c2=0

for i in range(0,len(n)):
    if(n[i]=='{'):
        c1+=1
    elif(n[i]=='}'):
        c1+=1
    elif(n[i]=='('):
        c2+=1
    elif(n[i]==')'):
        c2+=1


if(c1%2==0 and c2%2==0):
    print("1")
else:
    print("0")
