from gettext import c2py


class Customer:
    is_human = True # class instance variable
    def __init__(self,name,age,gender,city): # constructor
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city
    def describe(self): # instance method(function)
        print(f'Name:{self.name},Age:{self.age},Gender:{self.gender},City:{self.city}')
    def __str__(self): # __str__ is a special method(function) that is called when we call print()
        return f'Name:{self.name},Age:{self.age},Gender:{self.gender},City:{self.city}'

    def __eq__(self, other):
        return self.name == other.name
    def __eq__(self, other):
        return self.age == other.age
c1 = Customer("Yugank",24,"Male","India")
c2 = Customer("juliee",25,"Female","USA")
# c1.describe()
# c2.describe()
# print(c1)
if c1.name == c2.name:
    print("Same Name")
else:
    print("Not Same Name")
if c1.age == c2.age:
    print("Same Age")
else:
    print("Not Same Age")