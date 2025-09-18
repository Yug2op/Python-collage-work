class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def print_LL(head):
    while head is not None:
        print(head.value, end=' -> ')
        head = head.next
    print('end')

def get_tail(head):
    while head.next is not None:
        head = head.next
    return head

def insertAtTail(head,value):
    new_node = Node(value)
    if head is None:
        return new_node
    
    tail = get_tail(head)
    tail.next = new_node
    return head

head = None
head = insertAtTail(head,10)
head = insertAtTail(head,20)
head = insertAtTail(head,30)
head = insertAtTail(head,40)

print_LL(head)

    

    