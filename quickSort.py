def partition(arr,s,e):
    j = s
    i = s
    pivot = arr[e]
    
    while j<e:
        if arr[j] < pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j += 1
        else:
            j += 1
    arr[i],arr[e] = arr[e],arr[i]
    return i

def quick_sort(arr,s,e):
    #base case
    if s >= e : return
    # recursive case
    p_index = partition(arr,s,e)
    quick_sort(arr,s,p_index-1)
    quick_sort(arr,p_index+1,e)
    
    
arr =  list(map(int,input().split()))
n = len(arr)
quick_sort(arr,0,n-1)
print(arr)
