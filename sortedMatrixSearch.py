# staircase search
def iss_present(nums,target):
    m = len(nums)
    n = len(nums[0])
    i = 0
    j = n-1
    while i<m and j>=0:
        if nums[i][j] == target:
            return True
        elif nums[i][j] < target:
            i += 1
        else:
            j -= 1
    return False

nums = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 0
print(iss_present(nums,target))

# time: O(m+n)
# space: O(1)


