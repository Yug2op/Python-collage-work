a = int(input("Enter a number: "))
b = int(input("Enter diffrence: "))
r = int(input("Enter range: "))


for i in range(r):
    c = a + i * b
    print(c , end=', ')
    
