def greatestInLeft(arr,n):
    stack = []
    ans = []
    for i in range(n):
        while len(stack) != 0 and stack[-1] <= arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    return ans
    


arr = [5,3,6,7,2,1,4]
n = len(arr)
stack = [] # monotonic stack
ans = []

for i in range(n-1,-1,-1):
    # find the nearest greater element to the right of arr[i]
    
    while len(stack) != 0 and stack[-1] <= arr[i]:
        stack.pop()
    if len(stack) == 0:
        # arr[i] doesn't have any greater element to its right
        ans.append(-1)
    else:
        ans.append(stack[-1])
    stack.append(arr[i])
    
ans.reverse()

print(ans)

print(greatestInLeft(arr,n))