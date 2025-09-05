n = int(input())
nums = []
for i in range(n):
    digit = int(input())
    if digit == 0 or digit == 1:
        nums.append(digit)
nums.sort()
for num in nums:
    print(num, end=' ')