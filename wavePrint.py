nums = [[10,20,30],
        [40,50,60],
        [70,80,90],
        [100,110,120]]

m = 4
n = 3
for j in range(n):
    if j%2 == 0:
        for i in range(m):
            print(nums[i][j], end = " ")
    else:
        for i in range(m-1,-1,-1):
            print(nums[i][j], end = " ")   