def f(stack,val):
    # base case
    if len(stack) == 0:
        stack.append(val)
        return
    # recursive case
    x = stack.pop()
    
    f(stack,val)
    
    stack.append(x)
    
    


stack = [10,20,30,40,50]
val = 0
print(stack)
f(stack,val)
print(stack)