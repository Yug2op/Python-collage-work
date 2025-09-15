def print_path(paath,m,n):
    for i in range(m):
        for j in range(n):
            print(paath[i][j], end=" ")
        print()
    print()

def f(mat,m,n,i,j,paath):
    # base case
    if i == m or j == n:
        return 

    if mat[i][j] == 'x':
        return

    if i == m-1 and j == n-1:
        paath[i][j] = '1'
        print_path(paath,m,n)
        paath[i][j] = '0'
    # recursive case
    paath[i][j] = '1'
    f(mat,m,n,i,j+1,paath)
    f(mat,m,n,i+1,j,paath)
    paath[i][j] = 0
    return

mat = [[0,0,0,0],
       [0,0,'x',0],
       [0,0,0,'x'],
       [0,'x',0,0]]

m = len(mat)
n = len(mat[0])

paath = [[0]*n for _ in range(m)]

f(mat,m,n,0,0,paath)