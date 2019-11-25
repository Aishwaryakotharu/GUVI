n=input()
l=len(n)-1
a=list(n)
t=a[0]
a[0]=a[l]
a[l]=t
n=''.join(map(str,a))
print(n)