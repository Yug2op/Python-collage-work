class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_LL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

def insert_at_head(head,val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

def get_tail(head):
    while head.next is not None:
        head = head.next
    return head

def insert_at_tail(head,val):
    new_node = ListNode(val)
    tail = get_tail(head)
    tail.next = new_node
    return head

head = None
head = insert_at_head(head,10)
head = insert_at_head(head,20)
head = insert_at_head(head,30)
head = insert_at_head(head,40)
head = insert_at_head(head,50)
print_LL(head)

def delete_head(head):
    if head is None: # LL has no node
        return None
    return head.next

def delete_tail(head):
    if head is None: # LL has no node
        return None
    if head.next is None: # LL has only one node
        return None
    current = head
    previous = None
    while current.next is not None:
        previous = current
        current = current.next
    previous.next = None
    return head

head = delete_head(head)
print_LL(head)

head = insert_at_tail(head,60)
print_LL(head)

head = delete_tail(head)
print_LL(head)


