def maxArea(height):
    i = 0
    j = len(height)-1
    # print(height[i],height[j],(j-i))
    # print(min(height[i], height[j]) * (j-i))

    msf = 0
    while i<j:
        area = min(height[i], height[j]) * (j-i)
        msf = max(area,msf) 
        
        if height[i] < height[j]:
            i += 1 
        else:
            j -= 1
    return msf
    
        
n = int(input())
if n == 1:
    print("For container we need at least two inputs")
else:
    height = [0] * n
    for i in range(n):
        height[i] = int(input())
    print(maxArea(height))