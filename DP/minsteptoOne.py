def f_bottomup(n):
    
    dp = [None] * (n+1)
    dp[1] = 0
    
    for i in range(2,n+1):
        op1 = dp[i-1]
        op2 = float('inf')
        if i % 2 == 0:
            op2 = dp[i//2]
        op3 = float('inf')
        if i % 3 == 0:
            op3 = dp[i//3]
        dp[i] = 1 + min(op1,op2,op3)
    return dp[n]
n = int(input())
print(f_bottomup(n))