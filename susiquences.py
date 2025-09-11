def f(s,out,i):
    # base case
    if i == len(s):
        print("".join(out))
        return
    # recursive case
    
    
    # case1: include s[i] to out[]
    out.append(s[i])
    f(s,out,i+1)
    
    
    out.pop() # backtrack
    
    # case2: exclude s[i] from out[] 
    
    
    f(s,out,i+1)
    
    


s = "abc"
out = []
f(s,out,0)