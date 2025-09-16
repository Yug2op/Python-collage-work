def last_occ(arr,target):
    l = 0
    h = len(arr) - 1
    result = -1
    while l<=h:
        m = (l+h) // 2
        if arr[m] == target:
            result = m
            l = m + 1
        elif arr[m] > target:
            h = m-1
        else:
            l = m+1
    return result







arr = [10,30,30,40,50,60,60,70,70]
target = 30
print(last_occ(arr,target))
