class p:
    def __init__(self,age=0):
        self.age=age
        
    def get_age(self):
        return self.age
    def set_age(self,n):
        self.age=n
p1=p()
p1.set_age(21)
print(p1.age)