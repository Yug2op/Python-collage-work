arr = (1,2,3,4,5)
slc = arr[1:4]
print(slc)
print (arr[:])

def search(tup, val):
    for num in tup:
        if num == val:
            return True
    return False
print(search(arr, 3))
print(search(arr, 6))

val = 5
print(val in arr) # checking if val is present in arr or not