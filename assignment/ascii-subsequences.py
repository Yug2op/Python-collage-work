def charToNum(ch):
    return str(ord(ch))
def f(s,i,out,count,res):
    if i == len(s):
        res.append(("".join(out)))
        count[0] += 1
        return
    ch = s[i]
    asciiVal = charToNum(ch)
    
    f(s,i+1,out,count,res)
    out.append(ch)
    f(s,i+1,out,count,res)
    out.pop()

    out.append(asciiVal)
    f(s,i+1,out,count,res)
    out.pop()
    return count
    
    
        
    
    


s = list(input())
out =[]
count = [0]
res = []
f(s,0,out,count,res)
print(" ".join(res))
print(count[0])