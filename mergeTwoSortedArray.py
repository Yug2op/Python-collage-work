# Home Work
def merge_array(arr1,arr2,n,m,i,j):
    
    #[1,3,5,7] #[2,4,6,8,9]
    out = []
    while i<n and j<m:
        if arr1[i] <= arr2[j]:
            out.append(arr1[i])
            i += 1
        else:
            out.append(arr2[j])
            j += 1
    
    while i < n:
        out.append(arr1[i])
        i += 1
    while j < m:
        out.append(arr2[j])
        j += 1
    return out

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
print(merge_array(arr1,arr2,len(arr1),len(arr2),0,0)) 