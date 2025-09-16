arr = [(2,3), (1,2), (4,1), (3,4)]
sorted_arr = sorted(arr, key=lambda a : a[1])
print(sorted_arr)

# lambda function can be created and consumed in the same line
sum = lambda a, b : a+b
print(sum(10, 20))
print((lambda a, b : a+b)(10, 20))
print((lambda a, b : a if a>b else b)(10, 20))

# Normal function
def add(a, b):
    return a + b

# Lambda function (same thing in one line)
add_lambda = lambda a, b: a + b

print(add(5, 3))        # 8
print(add_lambda(5, 3)) # 8
