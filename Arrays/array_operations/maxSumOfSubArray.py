def max_subArray(arr,n):
    msf = float('-inf')
    for i in range(n):
        for j in range(i,n):
            s=0
            for k in range(i,j+1):
                s+= arr[k]
            msf = max(msf,s)
    return msf
# Time: O(n^3)
# Space: O(1)


def max_subArray_pSum(arr,n):
    psum = [0]*n
    psum[0] = arr[0]
    for i in range(1,n):
        psum[i] = psum[i-1] + arr[i]
    msf = float('-inf')
    for i in range(n):
        for j in range(i,n):
            s = psum[j] if i == 0 else psum[j] - psum[i-1]
            msf = max(msf,s)
    return msf
# Time: O(n^2)
# Space: O(n)

arr = [-2,1,-3,4,-1,2,1,-5,4]
n = len(arr)
print(max_subArray(arr,n))
print(max_subArray_pSum(arr,n))