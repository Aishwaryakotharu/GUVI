l=list()
s=0
a=0
for i in range(0,4):
    a=int(input("enter marks for"+i+" 4 subjects"))
    l.append(a)
    s=s+a
print("the subject marks:",l)
print("the sum of all subjects:",s)
a=s/4
print("the average is:",a)