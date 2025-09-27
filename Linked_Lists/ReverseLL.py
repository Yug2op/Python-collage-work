class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
def print_LL(head):
    while head is not None:
        print(head.value,end=' -> ')
        head = head.next
    print('end')
    
def reverse_LL(head):
    prev = None
    cur = head
    while cur is not None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev
        
head = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print_LL(head)

head = reverse_LL(head)

print_LL(head)

# [HW] Reverse recursively