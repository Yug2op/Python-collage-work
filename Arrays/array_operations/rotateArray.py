arr = [10,20,30,40,50,60,70]
n = 20
n = n % len(arr)

for _ in range(n):

    for ele in range((len(arr)-1), 0, -1):
        arr[ele], arr[ele-1] = arr[ele-1], arr[ele]
        
print(arr)