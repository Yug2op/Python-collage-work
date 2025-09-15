# Program to perform linear search on a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, data):
    if head is None:
        head = Node(data)
        return head

    current = head

    while current.next:
        current = current.next

    current.next = Node(data)
    
    return head

def linear_search(head, target):
    current = head

    while current:
        if current.data == target:
            return True

        current = current.next

    return False

def linear_search_recursive(head, target):
    # base case
    if head is None:
        return False
    # search for target
    if head.data == target:
        return True
    # recursive case
    return linear_search_recursive(head.next, target)

head = None

n = int(input("Enter the number of elements in the linked list: "))

print("Enter the elements of the linked list: ")
for i in range(n):
    data = int(input())
    head = insert_at_end(head, data)

target = int(input("Enter the element to search for: "))

# if linear_search(head, target):
#     print(f"{target} is present in the linked list.")
# else:
#     print(f"{target} is not present in the linked list.")
if linear_search_recursive(head, target):
    print(f"{target} is present in the linked list.")
else:
    print(f"{target} is not present in the linked list.")
