def smallestInLeft(arr,n):
    stack = []
    ans = []
    for i in range(n):
        while len(stack) != 0 and stack[-1] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    return ans




def smalleseInRight(arr,n):
    stack = []
    ans = []
    for i in range(n-1,-1,-1):
        
        while len(stack) != 0 and stack[-1] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    ans.reverse()
    return ans
        
        
        
        
arr = [9,5,2,3,1,6,7,4]
n = len(arr)

print(smalleseInRight(arr,n))
print(smallestInLeft(arr,n))
