# Sample Input
# 3
# 1 1 2
# Sample Output
# 2
# 1 2

n = int(input())
nums = list(map(int, input().split()))
nums = list(set(nums))  
print(len(nums))
nums.sort()
for num in nums:
    print(num, end=' ')