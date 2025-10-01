def f(p,i,j,y):
    
    # base case
    if i == j:
        return y* p[i]
    # recursive case
    return max (y*p[i] + f(p,i+1,j,y+1), y*p[j] + f(p,i,j-1,y+1))

p = [2,3,5,1,4]
n = len(p)
print(f(p,0,n-1,1))