l=[]
l.append(2)
l.append(3)
print(l)


x=l.copy()
print(type(x))
print(x)


l.clear()
print(l)

l=[2,2,3,4,'a']
print(l.count('a'))


x=(5,)
l.extend(x)
print(l)


print(l.index(5))


l.insert(5,'b')
print(l)


l.pop(1)
print(l)

l.insert(1,2)


l.remove(2)
print(l)


l.reverse()
print(l)

l=[3,1,5,8,1,2,9]
l.sort()
print(l)

