# def maxSubArraySum(arr,n):
#     x = [None]*n
#     x[0] = arr[0]
#     msf = x[0]
    
#     for i in range(1,n):
#         x[i] = max(x[i-1]+arr[i],arr[i])
#         msf = max(msf, x[i])
#     return msf
# time : O(n^2)
# space : O(n)

# enhanced formula
def maxSubArraySum(arr,n):
    x = arr[0]
    msf = x
    for i in range(1,n):
        x = max(x+arr[i],arr[i])
        msf = max(msf,x) 
    return msf
# time : O(n)
# space : O(1)


arr = [-3,2,-1,4,-5]

n = len(arr)

print(maxSubArraySum(arr,n))