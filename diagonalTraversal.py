# diagonal traversal
def print_diagonal(nums,m,n,i,j):
    while i<m and j<n:
        print(nums[i][j], end=" ")
        i += 1
        j += 1
    print()

nums = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
m = len(nums)
n = len(nums[0])
# starting point of form (0,0), (0,1), (0,2), (0,3)... => (0,j) where 0<=j<=n-1

for j in range(n):
    print_diagonal(nums,m,n,0,j)

# starting point of form (1,0), (2,0), (3,0)... => (i,0) where 0<=i<=n-1

for i in range(1,m):
    print_diagonal(nums,m,n,i,0)

    # length of diagonal from (i,j) = min(m-i,n-j)
    # time: O(mn)
    # space: O(1)