n=input()
n=list(n)
num=0
dig=0
special=0
for i in range(0,len(n)):
    if(ord(n[i])>64 and ord(n[i])<123):
        num+=1

    elif(ord(n[i])>47 and ord(n[i])<58):
        
        dig+=1
    else:
        print(n[i])
        special+=1
print(num,special,dig)