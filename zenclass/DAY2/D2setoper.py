s=set()
s.add("a")
s.add("b")
print(s)

s.clear()
print(s)

s={'a','b','c','hi'}
s1=s.copy()
print(s1,type(s1))
s2={'a','b','d','e'}
print(s1.difference(s2))


s1.difference_update(s2)
print(s1)

s.discard("hi")
print(s)

print(s.intersection(s2))

print(s.intersection_update(s2))

s={'a','b','c'}
s2={'c','d','e'}
print(s.isdisjoint(s2))

print(s.issubset(s2))

print(s.issuperset(s2))

s.pop()
print(s)

s.remove('b')
print(s)

print(s.symmetric_difference(s2))

a=s.symmetric_difference_update(s2)
print(s)