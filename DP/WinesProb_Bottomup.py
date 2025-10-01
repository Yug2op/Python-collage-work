def f_bottomUp(p,n):
    dp = [[None]*(n) for _ in range(n)]
    for i in range(n):
        dp[i][i] = n*p[i]
        
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            y = n-j+i
            dp[i][j] = max(y*p[i] + dp[i+1][j],y*p[j] + dp[i][j-1])
            
    return dp[0][n-1]

# [HW] space optimised to O(n)

def f_BUspaceopt(p,n):
    dp = [None] * n
    
p = [2,3,5,1,4]
n = len(p)

print(f_bottomUp(p,n))
print(f_BUspaceopt(p,n))

