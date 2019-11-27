n=input()
n=n[::-1]
n=list(n)
for i in range(0,2):
    n[i]=n[i].upper()
n=''.join(map(str,n))
print(n)

'''Sample Input :
jennyfer

Sample Output :
Refynnej'''