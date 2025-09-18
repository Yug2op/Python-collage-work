def search(arr,target,i,j):
    if i>j:
        return -1
    m = (i+j)//2
    if arr[m] == target:
        return m
    elif arr[m] > target:
        return search(arr,target,i,m-1)
    else:
        return search(arr,target,m+1,j)
    


n = int(input())
arr = list(map(int,input().split()))
target = int(input())
print(search(arr,target,0,n-1))