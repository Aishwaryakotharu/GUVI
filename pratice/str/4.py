n=input()
n=list(n)
s=0
for i in n:
    s=s+ord(i)
if(s%8==0):
    print("1")
else:
    print("0")