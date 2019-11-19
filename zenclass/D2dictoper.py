d={}
d[input()]=input()
print(d)


d.clear()
print(d)

d={'a':1,'b':2,'c':3,'d':4}
x=d.copy()
print(d,type(d))


x=('a','b')
y=1
d=dict.fromkeys(x,y)
print(d)

print(d.get('1'))
print(d.get('a'))

print(d.items())

print(d.keys())

d.pop("a")
print(d)

d={'a':1,'b':2,'c':3}
print(d)
d.popitem()
print(d)


x=d.setdefault('a')
print(x)

d.update({'a':3})
print(d)

print(d.values())