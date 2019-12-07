s1 = [];
s2 = [];

def eq(x):
    s1.append(x)


def dq():
    if (len(s2) == 0):
        if (len(s1) == 0):
            return 'Cannot dequeue because queue is empty'
    while (len(s1) > 0):
        p = s1.pop()
        s2.append(p)
    return s2.pop()


eq('a');
eq('b');
eq('c');
dq();
print(s1)
print(s2)