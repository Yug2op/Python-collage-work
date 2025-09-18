def maze(mat,n,m,i,j):
    # base case
    if mat[i][j] == 'x': # reached blocked cell
        return False
    if i == m-1 and j == n-1: # reached the destination
        return True

    # recursive case
    if i == m-1: # you are in in a cell in the last row
        return maze(mat,m,n,i,j+1)
    if j == n-1: # you are in in a cell in the last colum
        return maze(mat,m,n,i+1,j)

    # move right or move down
    return maze(mat,m,n,i+1,j) or maze(mat,m,n,i,j+1)
    


mat = [[0,0,0,0],
       [0,0,'x',0],
       [0,0,0,'x'],
       [0,'x',0,'x']]

m = len(mat)
n = len(mat[0])
print(maze(mat,n,m,0,0))