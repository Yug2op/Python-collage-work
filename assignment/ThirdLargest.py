def f(arr):
    if len(arr) < 3:
        arr = list(set(arr))
        arr.sort()
        return arr[-1]
    else:
        first = float('-inf')
        sec = float('-inf')
        third = float('-inf')
        for i in arr:
            if i > first:
                first,sec,third = i,first,sec
            elif i > sec and i != first:
                sec,third = i,sec
            elif i>third and i != sec and i != first:
                third = i
                
        if third == float('-inf'):
            return first
        else:
            return third
                    


arr = [1,2,3]
print(f(arr))
