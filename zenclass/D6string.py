n=input()

#input().split()
"""if we give n=input().split() 
    wont work for guvi but 
    will work for g*u*v*i then give input().split(*)"""


#it will not work str obj doesnt support assignment
"""for i in range(0,len(n)):
    n[i]=n[i].upper()
print(n)"""


#only char gets upper
"""for i in n:
    print(i.upper())"""


#to make entire list
n=list(n)
for i in range(0,len(n)):
    n[i]=n[i].upper()
a="".join(map(str,n))
print(a)


