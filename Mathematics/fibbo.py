n = int(input("Enter a number: "))
a =0
b =1


if n==0 or n==1:
    print("fibbo is: ",n)
else:
    i = 1
    while i<=n-1:
        c = a+b
        a=b
        b=c
        i+=1
    print("fibbo is: ",c)     
    # time complexity is O(n) linear time complexity
# space complexity is O(1) constant space complexity