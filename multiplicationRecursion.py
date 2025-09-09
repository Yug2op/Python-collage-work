def mul(n,m):
    if n==0 or m==0:
        return 0
    return n + mul(n,m-1)


n = int(input())
m = int(input())
print(mul(n,m))