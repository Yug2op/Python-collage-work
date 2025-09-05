def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

def print_pascals_triangle(rows):
    for n in range(rows):
        # Print leading spaces
        print('  ' * (rows - n - 1), end='')
        # Generate and print the row with tab separation
        row = [nCr(n, k) for k in range(n+1)]
        print('    '.join(map(str, row)))

# Get number of rows from user
n = int(input())
if 0 < n <= 10:
    print_pascals_triangle(n)
else:
    print("Please enter a positive integer less than or equal to 10.")