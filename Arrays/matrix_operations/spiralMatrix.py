# arr = [[11,12,13,14],
#        [15,16,17,18],
#        [19,20,21,22],
#        [23,24,25,26],
#        [27,28,29,30]] #  m x n
arr = [[1, 2, 3, 4], 
           [5, 6, 7, 8], 
           [9, 10, 11, 12], 
           [13, 14, 15, 16]]


m = len(arr)
n = len(arr[0])
top,bottom,left,right = 0,m-1,0,n-1
res = []
while bottom >= top and right >= left:
    for j in range(left,right+1):
        res.append(arr[top][j])
    top+=1
    
    for i in range(top,bottom+1):
        res.append(arr[i][right])
    right -= 1
    
    if top <= bottom:
        for j in range (right,left-1,-1):
            res.append(arr[bottom][j])
        bottom -= 1
    
    if left <= right:
        for i in range (bottom,top-1,-1):
            res.append(arr[i][left])
        left += 1
print(res) 
                
    