def move(m,n,i,j,res,count):
    if i == m or j==n:
        return 
    if i == m-1 and j == n-1:
        count[0] += 1
        print("".join(res),end=" ")
        return 
    res.append('V')
    move(m,n,i+1,j,res,count)
    res.pop()
    res.append('H')
    move(m,n,i,j+1,res,count)
    res.pop()
    res.append('D')
    move(m,n,i+1,j+1,res,count)
    res.pop()
        
        
    
        
        
    


m = int(input())
n = int(input())
res = []
count = [0]
move(m,n,0,0,res,count)
print("\n"+ str(count[0]))