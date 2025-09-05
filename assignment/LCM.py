num1 = int(input())
num2 = int(input())
def gdc(a,b):
    while b != 0:
        a,b = b,a%b
    return a

def lcm(a,b):
    return (a*b) // gdc(a,b)
print(lcm(num1,num2))
    
    