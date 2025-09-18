class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
def print_LL(head):
    while head is not None:
        print(head.value,end=' -> ')
        head = head.next
    print('end')
    
def has_cycle(head):
    s = set()
    while head is not None:
        if head in s:
            return True
        s.add(head)
        head = head.next
    return False
    
head = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)
head.next.next.next.next.next.next = head.next.next

print(has_cycle(head))



