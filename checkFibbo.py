n = int(input("Enter a number: "))
if n==0 or n==1:
    print(n, "is the fibbo number")
else:
    a=0
    b=1
    while True:
        c=a+b
        if c==n:
            print(n, "is a fibbo number")
            break
        if c>n:
            print(n, "is not a fibbo number")
            break
        a=b
        b=c
