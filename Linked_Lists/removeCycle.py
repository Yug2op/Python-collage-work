# floyds cycle detection is a cycle detection 
# algorithm used to detect the presence of a 
# cycle in a linked list.

# it works by using two pointers, one slow and one fast.
# the slow pointer moves one step at a time while 
# the fast pointer moves two steps at a time.
# if there is a cycle, the fast pointer will 
# eventually meet the slow pointer.
# if there is no cycle, the fast pointer will 
# reach the end of the linked list.

# time complexity: O(n)
# space complexity: O(1)

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
def print_LL(head):
    while head is not None:
        print(head.value,end=' -> ')
        head = head.next
    print('end')
    
def remove_cycle(head):
    if head is None:
        return False
    # find the intersection point
    slow = head
    fast = head
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # find the starting point
    slow = head
    while slow.next is not fast.next:
        slow = slow.next
        fast = fast.next
    fast.next = None
    return True
    
head = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)
head.next.next.next.next.next.next = head.next.next

# print_LL(head)


print(remove_cycle(head))
print_LL(head)