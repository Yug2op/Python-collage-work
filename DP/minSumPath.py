def min_sum_path(mat,m,n,i,j):
    # base case
    if i == m-1 and j == n-1:
        return mat[i][j]
    
    # recursive case
    if j == n-1:
        
        return mat[i][j] + min_sum_path(mat,m,n,i+1,j) 
    if i == m-1:
        
        return mat[i][j] + min_sum_path(mat,m,n,i,j+1)
    
    return mat[i][j] + min(min_sum_path(mat,m,n,i,j+1),min_sum_path(mat,m,n,i+1,j)) 
    

    
    
mat = [[1,3,1],
       [1,5,1],
       [4,2,1]]

m = len(mat)
n = len(mat[0])

print(min_sum_path(mat,m,n,0,0))