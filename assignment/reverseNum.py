def reverse(x):
    num = 0
    while x > 0:
        rem = x % 10 
        num = (num * 10 ) + rem
        x = x // 10
    return num

x = 120
print(reverse(x))