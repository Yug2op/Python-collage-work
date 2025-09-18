class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
def InAtPos(head,value,pos):
    new_node = Node(value)
    # case1 - Insert At Head If Node LL is Empty
    if pos == 1:
        new_node.next = head
        return new_node
    
    # case2 - Travers to Pos - 1
    
    temp = head
    count = 1
    while temp is not None and count < pos - 1:
        temp = temp.next
        count += 1
        
    # If pos is Invalid
    
    if temp is None:
        print('Invalid Position')
        return head
    
    # Insert at mid or tail
    
    new_node.next = temp.next
    temp.next = new_node
    return head
        
def print_LL(head):
    while head is not None:
        print(head.value, end=' -> ')
        head = head.next
    print('end')

head = None
head = InAtPos(head,10,1)
head = InAtPos(head,20,2)
head = InAtPos(head,30,3)
head = InAtPos(head,0,1)
head = InAtPos(head,25,4)
print_LL(head)