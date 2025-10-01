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
          # Backtrack to print path
        path = []
        i, j = 0, 0
        while not (i == m-1 and j == n-1):
            path.append((i, j))
            if i == m-1:        # last row → only right
                j += 1
            elif j == n-1:      # last col → only down
                i += 1
            else:
                if dp[i+1][j] < dp[i][j+1]:
                    i += 1      # move down
                else:
                    j += 1      # move right
        path.append((m-1, n-1))
    
        return dp[0][0],path
    
    
grid = [[1,3,1],[1,5,1],[4,2,1]]
m = len(grid)
n = len(grid[0])

print(f_bottomup(grid,m,n))