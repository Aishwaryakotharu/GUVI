a=int(input())
t=0
for i in range(0,a):
    for j in range(0,5):
        c=input("name:")
        m1=int(input("math:"))
        m2=int(input("science:"))
        m3=int(input("social science:"))
        m4=int(input("english:"))
        m5=int(input("cs:"))
        t=m1+m2+m3+m4+m5
        p=(t/125)*100
        print("sum:",t)    
        print("percentage",p)


