def print_num(n):
    if n == 0:
        return 0
    print_num(n-1)
    print(n, end = " ")

def print_num1(n):
    if n == 0:
        return 0
    print(n, end = " ")
    print_num1(n-1)


n=int(input())
print_num1(n)
print_num(n)

# time: O(n)
# space: O(n)