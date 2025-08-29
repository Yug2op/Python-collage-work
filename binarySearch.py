def binary_search(nums, target):
    l = 0
    h = len(nums) - 1
    while l <= h:
        m = (l+h) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            h = m - 1
    return -1


nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# target = int(input("Enter the target number: "))

# print("At index: ",binary_search(nums, target))


def first_Occ(nums1,target1):
    l = 0
    h = len(nums1) - 1
    result = -1
    while l <= h:
        m = (l+h) // 2
        if nums1[m] == target1:
            result = m
            h = m -1
        elif nums1[m] < target1:
            l = m +1
        else:
            h = m - 1
    return result

nums1 = [10,20,30,30,30,40,50]
target1 = int(input("Enter the target number to find first occurrence: "))
print("First occurrence at index: ",first_Occ(nums1,target1))