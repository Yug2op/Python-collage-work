def min_sum_pathTopdown(mat,m,n,i,j,dp):
    if i == m or j == n:
        return float('inf')
    
    if dp[i][j] != -1:
        return dp[i][j]
    # base case
    if i == m-1 and j == n-1:
        return mat[i][j]
    # recursive case
    
    dp[i][j] = mat[i][j] + min(min_sum_pathTopdown(mat,m,n,i,j+1,dp),min_sum_pathTopdown(mat,m,n,i+1,j,dp)) 
    return dp[i][j]

    
    
mat = [[1,3,1],
       [1,5,1],
       [4,2,1]]

m = len(mat)
n = len(mat[0])
dp = [[-1] *n for _ in range(m)]
print(min_sum_pathTopdown(mat,m,n,0,0,dp))

# f_bottomup(grid,m,n):
# dp = [[none] *n for _ in range(m)]
# for i in range(m-1,-1,-1):
# for j in range(n-1,-1,-1):
#   if i == m-1 and j == n-1:
#       dp[i][j] = grid[i][j]
#   elif i == m-1:
    # dp[i][j] = grid[i][j] + dp[i][j+1]
#   elif i == n-1:
    # dp[i][j] = grid[i][j] + dp[i+1][j]
#   else:
 #      dp[i][j] = grid[i][j] + min(dp[i+1][j],dp[i][j+1])
#  return dp[0][0]