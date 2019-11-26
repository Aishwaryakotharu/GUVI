p=input()
n=ord(p)
l=int(input())
for i in range(65,n+1):
    print(chr(i),end='')
    for j in range(1,l+1):
        print(j,end='')
    print("")