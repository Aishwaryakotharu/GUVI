n=input()
n=list(n)
l=len(n)
if(l%2==0):
    l=int(l//2)-1
    
    n[l]="*"
    n[l+1]="*"
    
else:
    
    l=int(l/2)
    n[l]="*"

n=''.join(map(str,n))
print(n)