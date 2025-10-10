# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# Example 3:

# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.


def mergeIntervals(arr):
    n = len(arr)
    # res = []
    i = 0
    while i < n-1:
        if arr[i][1] >= arr[i+1][0]:
            if arr[i][1] < arr[i+1][1]:
                arr[i] = [arr[i][0],arr[i+1][1]]
            else:
                arr[i] = [arr[i][0],arr[i][1]]
            arr.pop(i+1)
            n = len(arr)
            i = i
        else:
            i += 1
        
        
    return arr
    
# arr = [[1,3],[2,6],[8,10],[15,18]]
# arr = [[1,1],[2,2],[0,0],[2,3],[1,3],[3,5],[2,3],[3,5]]
# arr = [[1,4],[4,5]]
# arr = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
# arr = [[1,3],[2,6],[8,10],[8,9],[9,11],[15,18],[2,4],[16,17]]
# arr = [[1012,1136],[1137,1417],[1015,1020]]
# arr = [[1,3]]
arr = [[1,4],[2,3]]
arr.sort()
# print(arr)
# arr[0] = [arr[0][0],arr[1][1]]
# print(arr)
# print(arr.pop(1))
# print(arr)
print(mergeIntervals(arr))


                
        

