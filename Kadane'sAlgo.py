def maxSubArraySum1(arr,n):
    x = [None]*n
    x[0] = arr[0]
    msf = x[0]
    
    for i in range(1,n):
        x[i] = max(x[i-1]+arr[i],arr[i])
        msf = max(msf, x[i])
    return msf
# time : O(n^2)
# space : O(n)

# enhanced formula
def maxSubArraySum2(arr,n):
    x = arr[0]
    msf = x
    for i in range(1,n):
        x = max(x+arr[i],arr[i])
        msf = max(msf,x) 
    return msf
# time : O(n)
# space : O(1)


def maxSubArray( nums):
    n = len(nums)
    x = nums[0]
    msf = x
    for i in range(1,n):
        x = max(x+nums[i],nums[i])
        msf = max(msf,x)
    return (msf)


arr = [-3,2,-1,4,7] # => [-3,-1,-2,2,9]
# arr = [-27,-43,-48,-22,-11]

n = len(arr)

print(maxSubArray(arr))
print(maxSubArraySum1(arr,n))
print(maxSubArraySum2(arr,n))