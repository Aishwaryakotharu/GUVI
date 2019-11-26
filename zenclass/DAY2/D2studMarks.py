l=list()
s=0
a=0
for i in range(0,4):
    a=int(input("subject %d"%i))
    for j in range(0,5):
        b=int(input("subject %d"%j))
        l.push(a)
        l.push(b)
        s=s+l[i]
print(l)
print(s)
a=s/4
print(a)