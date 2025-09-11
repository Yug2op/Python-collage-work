def isArraySorted(arr,n,i):
    # base case
    if i == n-1:
        return True
    
    # recursive case
    return arr[i]<arr[i+1] and isArraySorted(arr,n,i+1)
  
    
n = int(input())
arr = list(map(int,input().split()))
print(isArraySorted(arr,n,0))