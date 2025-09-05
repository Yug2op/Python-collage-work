# def genPairs(arr,n,target):
#     count = 0
#     for i in range(0,n-1):
#         for j in range(i+1,n):
#             if arr[i]+arr[j] == target:
#                 count +=1
            
#     return count
def genPairs(arr,n,target):
    count = 0
    i = 0
    j = n-1
    while i<j:
        sum = arr[i]+arr[j]
        if sum == target:
            count += 1
            i += 1
            j -= 1
        elif sum > target:
            j -= 1
        else:
            i += 1
    return count
        
arr = [10,20,30,40,50,60]
n = len(arr)
target = 60

print(genPairs(arr,n,target))