def diaSort(nums,m,n,i,j):
    x,y = i,j
    dia = []
    while x<m and y<n:
        dia.append(nums[x][y])
        
        x += 1
        y += 1
    dia.sort()
    x,y = i,j
    for val in dia:
        nums[x][y] = val
        x += 1
        y += 1
        
    return dia
    
    
    

nums = [[50,80,20],
        [90,10,70],
        [60,30,40]]
m = len(nums)
n = len(nums[0])
for i in range(m):
    diaSort(nums,m,n,i,0)
for j in range(1,n):
    diaSort(nums,m,n,0,j)

print(nums)
    

