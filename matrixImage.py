def matImg(nums,n):
    imag = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            a = imag[i][j] = nums[n-1-j][i]
            print(a, end=' ')
        print()
    


nums = [[1,2,3],
        [4,5,6],
        [7,8,9]]

n = m = len(nums)

matImg(nums,n)