n = int(input("Enter a number: "))
m = int(input("Enter the precision: "))
div = 1
ans = 0
for i in range(m):
    div = div * 10
    while ans*ans <= n:
        ans += 1/div
    ans = ans - 1/div
print(round(ans,m))
    
