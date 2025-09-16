arr = [10,20,30,40,50,60,70]
k = 21
n = len(arr)
k = k%n # in case k>n

i = 0
j = n-1
while i<j:
    arr[i], arr[j] = arr[j], arr[i]
    i+=1
    j-=1

i = 0
j = k-1
while i<j:
    arr[i], arr[j] = arr[j], arr[i]
    i+=1
    j-=1

i = k
j = n-1
while i<j:
    arr[i], arr[j] = arr[j], arr[i]
    i+=1
    j-=1

print(arr)    