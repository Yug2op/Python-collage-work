def f(mat,m,n,i,j):
    # base case
    if i == m or j == n:
        return 0

    if mat[i][j] == 'x':
        return 0


    if i == m-1 and j == n-1:
        return 1
    

    return f(mat,m,n,i+1,j) + f(mat,m,n,i,j+1)

mat = [[0,0,0,0],
       [0,0,'x',0],
       ['x',0,0,'x'],
       [0,'x',0,0]]

m = len(mat)
n = len(mat[0])

print(f(mat,m,n,0,0))