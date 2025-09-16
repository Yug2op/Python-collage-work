arr = [1,2,3,4,5] # This is a list in Python similar to tuple

#tuple are imutable but list are mutable
# tup = (1,2,3,4,5) # This is a tuple in Python


print(type(arr))
print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[2])

arr[0] = 20

for i in arr:
    print(i, end=' ')

print()
print(sum(arr))
print(max(arr))
print(min(arr))
key = 3

print(key in arr)    

l = list("Yugank")

print(l)

slice = arr[1:4] # slicing in list
print(slice)
slice[0] = 100
print(slice)
print(arr) # original list is not affected

colors = ['red', 'green', 'blue', 'white']
for c in colors:
    print(c, end=' ')
print()
colors[1:3] = ['yellow', 'black'] # replacing a part of list
for c in colors:
    print(c, end=' ')
print()

colors[1:3] = ['pink']
print(colors)
print(len(colors))
colors[1:1] = ['purple', 'orange'] # inserting elements at index 1
print(colors)
print(len(colors))
colors[1:4] = [] # deleting elements from index 1 to 3
print(colors) 
print(len(colors))  

colors.insert(0, 'cyan') # inserting element at index 1
print(colors)
colors.append('magenta') # inserting element at the end
print(colors)
colors.remove('white') # removing element
print(colors)
colors.pop() # removing last element
print(colors)
colors.insert(2, 'brown') # inserting element
colors.insert(3, 'blue') # inserting element 
colors.insert(4, 'green') # inserting element
print(colors)
colors.pop(0) # removing element at index 0
print(colors)

nums = [5, 3, 8, 6, 7, 2]
print(nums, len(nums))
print(arr)

nums.extend(arr) # adding elements of arr to nums
print(nums , len(nums))

