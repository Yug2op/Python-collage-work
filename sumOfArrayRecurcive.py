def arraySum(arr:list[int], n:int, i:int)->int:
    # base case
    if i == n-1:
        return arr[n-1]
    # recursive case
    
    # f(i) = find the sum of x[i.....n-1]
    
    # ask your friend to find the sum of x[i+1.....n-1]
    
    return arr[i] + arraySum(arr,n,i+1)
    



    
n = int(input())
arr = list(map(int,input().split()))
print(arraySum(arr,n,0))