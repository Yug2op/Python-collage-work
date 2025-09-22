def f(arr,k):
    arr = list(set(arr))
    if len(arr) < k:
        arr.sort()
        return (arr[-1])
    else:
        newArr = [float('-inf')] * k
        for num in arr:
            for i in range(k):
                if num > newArr[i]:
                    newArr[i+1:k] = newArr[i:k-1]
                    newArr[i] = num
                    break
        if newArr[k-1] == float('-inf'):
            return newArr[k-2]
        else:
            return newArr[k-1]                                  


arr = [1,1,3,3]
k = 1
print(f(arr,k))