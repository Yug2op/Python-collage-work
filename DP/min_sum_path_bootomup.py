def f_bottomup(grid,m,n):
    dp = [[None] *n for _ in range(m)]
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i == m-1 and j == n-1:
                dp[i][j] = grid[i][j]
            elif i == m-1:
                dp[i][j] = grid[i][j] + dp[i][j+1]
            elif j == n-1:
                dp[i][j] = grid[i][j] + dp[i+1][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i+1][j],dp[i][j+1])
    return dp[0][0]



def f_BUspaceOpt(mat,m,n):
    dp = [None] * n
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i == m-1 and j == n-1:
                dp[j] = mat[i][j]
            elif i == m-1:
                dp[j] = mat[i][j] + dp[j+1]
            elif j == n-1:
                dp[j] = mat[i][j] + dp[j]
            else:
                dp[j] = min(mat[i][j] + dp[j+1],mat[i][j] + dp[j])
    return dp[0]    
                
                
mat = [[1,3,1],
       [1,6,4],
       [7,2,1]]

m = len(mat)
n = len(mat[0])
print(f_bottomup(mat,m,n))
print(f_BUspaceOpt(mat,m,n))
