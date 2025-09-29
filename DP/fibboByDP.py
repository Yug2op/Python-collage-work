def f(n, dp):
    if dp[n] != -1:
        return dp[n]
    
    if n == 0 or n == 1:
        dp[n] = n
        return n
    
    dp[n] = f(n-1, dp) + f(n-2, dp)
    return dp[n]

n = int(input())
dp = [-1] * (n + 1)
print(f(n, dp))
# top-down approach / memoization
# time complexity: O(n)
# space complexity: O(n)

def f_bottomup(n,dp1):
    dp1[0] = 0
    dp1[1] = 1
    
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

n = 8
dp1 = [None] * (n+1)
print(f_bottomup(n,dp1))

# bottom-up approach / tabulization
# time complexity: O(n)
# space complexity: O(n)



