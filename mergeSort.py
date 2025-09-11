def merge(arr,s,e):
    m = (s+e)//2
    
    i,j = s,m+1
    
    out = []
    
    while i<=m and j<=e:
        if arr[i] <= arr[j]:
            out.append(arr[i])
            i += 1
        else:
            out.append(arr[j])
            j += 1
            
    while i <= m:
        out.append(arr[i])
        i+=1
    while j <= e:
        out.append(arr[j])
        j+=1
        
        
    arr[s:e+1] = out
def merge_sort(arr,s,e):
    # base case
    if s == e:
        return
    
    # recursive case
    
    m = (s+e)//2
    
    merge_sort(arr,s,m)
    merge_sort(arr,m+1,e)
    merge(arr,s,e)


    
n = int(input())
arr = list(map(int,input().split()))
merge_sort(arr,0,n-1)
print(arr)