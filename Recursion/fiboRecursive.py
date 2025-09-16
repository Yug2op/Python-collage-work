def fibo(n):
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    # recursive case
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))
# followes depth first search
# time: O(2^n)
# space: O(n)