def step_to_one(n):
    # base case
    if n == 1:
        return 0
    # recursive case
    
    x = step_to_one(n-1)
    y = float('inf')
    if n % 2 == 0:
        y = step_to_one(n/2)
    z = float('inf')
    if n % 3 == 0:
        z = step_to_one(n/3)
    
    return 1 + min(x,y,z)
n = 500
print(step_to_one(n))


# using dp
def step_to_one1(n,dp):
    
    # base case
    if n == 1:
        return 0
    
    #lookups
    if dp[n] != -1:
        return dp[n]
    
    # recursive case
    
    x = step_to_one1(n-1,dp)
    
    y = float('inf')
    if n % 2 == 0:
        y = step_to_one1(n // 2,dp)
    z = float('inf')
    if n % 3 == 0:
        z = step_to_one1(n // 3,dp)
    
    dp[n] = 1 + min(x,y,z)
    return dp[n]

# n = 5
dp = [-1] * (n+1)
print(step_to_one1(n,dp))