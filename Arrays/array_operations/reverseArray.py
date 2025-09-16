n = int(input("Enter number of elements : "))
list = [int(input()) for _ in range(n)]
print("Original array:", list)

def reverseArray(list):
    i =0
    j = len(list)-1
    while i<j:
        list[i],list[j] = list[j],list[i]
        i+=1
        j-=1
reverseArray(list)
print("Reversed array:", list)
