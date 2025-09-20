def move(n,i,j,res="",count = [0]):
    if i == n or j == n:
        return 
    if i == n-1 and j == n-1:
        count[0] += 1
        print(res,end=" ")
        return 
    
    move(n,i+1,j,res+"V")
    move(n,i,j+1,res+"H")
    if (i == j) or (i+j ) == n-1:
        move(n,i+1,j+1,res+"D")
    
    return(count[0])



n = int(input())

print("\n"+str(move(n,0,0)))