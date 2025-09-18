class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
def InsertAtHead(head,val):
    new_node = Node(val)
    new_node.next = head
    return new_node

def print_LL(head):
    while head is not None:
        print(head.value, end=" ")
        head = head.next
    print('END')

head = None
head = InsertAtHead(head,50)    
head = InsertAtHead(head,40)    
head = InsertAtHead(head,30)    
head = InsertAtHead(head,20)    
head = InsertAtHead(head,10)    

print_LL(head)

