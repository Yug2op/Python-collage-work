def replace(n):
    # basecase
    if n == 0:
        return 0
    # recursive case
    rem = n % 10
    if rem == 0:
        rem = 5
    return replace(n//10) * 10 + rem


n = int(input())
print(replace(n))