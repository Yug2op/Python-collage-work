def priffixSum(arr,n):
    psum = [None] * n
    psum[0] = arr[0]
    for i in range(1,n):
        psum[i] = psum[i-1] + arr[i]
    return psum

arr = [1,2,3,4,5,6]
n = len(arr)
print(priffixSum(arr,n))