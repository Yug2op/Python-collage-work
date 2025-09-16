x=10
y=x
k="hello"
z=3.14
is_active=True
sum_value=1+2
print(x, type(x))
print(k, type(k))
print(z, type(z))
print(is_active, type(is_active))
print(sum_value, type(sum_value))
print(x, id(x))
print(y, id(y))
print(x is y)
m=10
print(m, id(m))
print(x is m)

del x
print(y)
print(m)
# print(x) # will give error as x is deleted