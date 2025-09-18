class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
def print_LL(head):
    while head is not None:
        print(head.value,end=' -> ')
        head = head.next
    print('end')
    
def mid_point(head):
    if head is None:
        return None
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
    
head = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
# head.next.next.next = Node(40)
# head.next.next.next.next = Node(50)
# head.next.next.next.next.next = Node(60)

# print_LL(head)cls


midpoint = mid_point(head)

if mid_point is not None:
    print(midpoint.value)
else:
    print('Node is empty')
    
    
# [do it again]