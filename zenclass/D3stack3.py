class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):   
        return self.items == []
  
    def push(self, item):
        self.items.insert(0,item)
    
    def pop(self):
        return self.items.pop(0)
    
s=Stack()
s.push('a')
s.push('b')
print(s.pop())
