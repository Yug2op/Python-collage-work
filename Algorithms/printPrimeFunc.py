num = int(input("Enter a num: "))

def isPrime(a):
    i = 2
    while i <= int(a ** 0.5):
        if a%i==0:
            return False
        i += 1
    return True        
print(isPrime(num))

def printPrime(m):
    for i in range(2,m+1):
        if isPrime(i):
            print(i)
printPrime(20)            
            
            