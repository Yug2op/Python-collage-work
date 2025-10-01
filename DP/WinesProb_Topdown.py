def f_topdown(p,i,j,y,dp):
    #lookup
    if dp[i][j][y] != -1:
        return dp[i][j][y]
    # base case
    if i == j:
        return y* p[i]
    # recursive case
    
    dp[i][j][y] = max (y*p[i] + f_topdown(p,i+1,j,y+1,dp), y*p[j] + f_topdown(p,i,j-1,y+1,dp))
    return dp[i][j][y]
p = [6,1,2,9,4]
n = len(p)
dp = [[[-1]*(n+1) for _ in range(n)] for _ in range(n)]
# print(f_topdown(p,0,n-1,1,dp))











def f_topdown2(p2,i,j,dp2):
    m = len(p2)
    y = m-j+i
    #lookup
    if dp2[i][j] != -1:
        return dp2[i][j]
    # base case
    if i == j:
        return y* p2[i]
    # recursive case
    dp2[i][j] = max (y*p2[i] + f_topdown2(p2,i+1,j,dp2), y*p2[j] + f_topdown2(p2,i,j-1,dp2))
    return dp2[i][j]

p2 = [6,1,2,9,4]
m = len(p2)
dp2 = [[-1]*(m) for _ in range(m)]
print(f_topdown2(p2,0,m-1,dp2))

for i in range(m):
    for j in range(m):
        print(dp2[i][j],end=' ')
    print()
    