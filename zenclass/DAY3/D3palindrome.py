n=input()

r=0
l=len(n)
n=int(n)
temp=n
while(n>0):
    x=n%10
    r=(r*10)+x
    n=n//10
print(r)
print(temp)
if(temp==r):
    print("palindrome")
else:
    print("not palindrome")