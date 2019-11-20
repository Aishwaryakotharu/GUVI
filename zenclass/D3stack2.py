l=[]
l2=[]
def push(a,b):
    a.append(b)
def pop(a):
    return a.pop()

push(l,'a')
push(l,'b')
push(l2,'1')
pop(l)
pop(l2)
print(l)
print(l2)