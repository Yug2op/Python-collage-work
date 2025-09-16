def add (a,b,c):
    return a+b+c
print(add(2,3,4))
# print(add(2,3,4,5)) error # TypeError: add() takes 3 positional arguments but 4 were given
# print(add(2,3)) # TypeError: add() missing 1 required positional argument: 'c'
# to avoid this we use optional arguments
def add2 (a,b,c=0,d=0):
    return a+b+c+d  
print(add2(2,3,4,5))
print(add2(2,3,4))
print(add2(2,3))
print(add2(2,3,d=5))

def add3 (a,b,*c):
    print(a,b,c)
    print(type(a), type(b), type(c))
    return a+b+sum(c)
print(add3(2,3,4,5,6,7,8,9))
print(add3(2,3))

def add4(*a,b):
    print(a,b)
    print(type(a), type(b))
    return sum(a)+b
# print(add4(2,3,4,5,6,7,8,9,10)) # TypeError: add4() missing 1 required keyword-only argument: 'b'
print(add4(2,3,4,5,6,7,8,9,b=10))