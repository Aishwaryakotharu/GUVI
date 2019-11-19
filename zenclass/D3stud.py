a=int(input())
t=0
p=0
for j in range(1,5):
    c=input("name:")
    m1=int(input("math:"))
    m2=int(input("science:"))
    m3=int(input("social science:"))
    m4=int(input("english:"))
    m5=int(input("cs:"))
    t=m1+m2+m3+m4+m5
    p=float((t/125)*100)
    print("sum:",t)    
    print(p)
    if(p>=90):
            print("iit")
    elif(p>=80 and p<90):
            print("anna university")
    elif(p>=70 and p<80):
	    print("mgit")
    elif(p<70):
	    print("rejected")
