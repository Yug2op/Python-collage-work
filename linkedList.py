# link list is a data structure in which 
# each element is connected to the next element 
# by address of next element.
# each element is called node and each node has two parts
# 1. data
# 2. pointer to the next node

# types of link list
# 1. singly link list
# 2. doubly link list
# 3. circular link list

# singly link list is a link list in which 
# each node has a pointer to the next node
# and last node has a pointer to None

# example
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

# l1 = Node(10)  
# l2 = Node(20)
# l1.next = l2
# l3 = Node(30)
# l2.next = l3
# l4 = Node(40)
# l3.next = l4
# l5 = Node(50)   
# l4.next = l5
# l5.next = None
# print(l1)
# print(l2)
# print(l3)
# print(l4)
# print(l5)

head = None # head is a pointer to the first node

head = Node(10) # first node
head.next = Node(20) # second node
head.next.next = Node(30) # third node
head.next.next.next = Node(40) # fourth node
head.next.next.next.next = Node(50) # fifth node
head.next.next.next.next.next = None # last node

while head is not None:
    print(head.data)
    head = head.next

# doubly link list is a link list in which 
# each node has a pointer to the next node
# and last node has a pointer to None
# and each node has a pointer to the previous node

# circular link list is a link list in which 
# last node has a pointer to the first node
# and first node has a pointer to the next node


