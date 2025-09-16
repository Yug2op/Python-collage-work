num = [1,2,3,4,5]
squares = []
for n in num:
    squares.append(n*n)
print(squares)

nums2 = [10,20,30,40,50]
squares2 = [n*n for n in nums2]
print(squares2)

arr = []
for _ in range(5):
    arr.append(int(input()))
print(arr)

# OR

arr2 = [int(input()) for _ in range(5)]
print(arr2)

arr1 = [1,2,3,4,5]
arr5 = [n**3 if n%2 == 0 else n**2 for n in arr1]
print(arr5)