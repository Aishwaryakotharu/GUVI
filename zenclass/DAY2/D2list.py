l=list()
s=0
av=0
for i in range(0,4):
    a=int(input("enter marks subject %d :",%(i)))
    l.append(a)
    s=s+a
print("the subject marks:",l)
print("the sum of all subjects:",s)
av=s/4
print("the average is:",av)