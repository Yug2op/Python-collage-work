# every subArray have a static array starting from 0 to n-1 and ending from i to n
def generate_subarrays(arr, n):
    for i in range(n): # 0 <= i <= n-1
        for j in range(i, n): # i <= j <= n-1
            for k in range(i, j + 1):
                print(arr[k], end=' ')
            print()
# for array of size of n we have n(n+1)//2 sub arrays
# for 5, 5(6)//2 = 15 sub arrays
            
            

arr = [1, 2, 3, 4, 5]
n = len(arr)
generate_subarrays(arr, n)