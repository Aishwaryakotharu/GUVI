a=int(input())
b=int(input())
p=int(input())
d=b-a
if(d>5):
    e=d-5
    print(e)
    price=(e*8)+100
    if(p==1):
        price=price+(price*0.25)
    
else:
    price=100
    if(p==1):
        price=price+(price*0.25)
         
print(price)