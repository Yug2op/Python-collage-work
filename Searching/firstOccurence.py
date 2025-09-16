def first_occurrence(arr, target):
    low = 0
    high = len(arr)-1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1  # continue searching in the left half
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return result
        
arr = [10,20,30,30,30,40,50]
target = int(input("Enter the target number to find first occurrence: "))
print("First occurrence at index: ",first_occurrence(arr,target))


# learn bisect module for python
