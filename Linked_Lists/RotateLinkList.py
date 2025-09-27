class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
    
head = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

# 10 20 30 40 50
# for k = 2
# 40 50 10 20 30
k = int(input())
def rotateList(head,k):
    # calculate length
    l = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        l += 1
        
    # head 10 20 30 40 50 tail
        
    # make it circular LL
    tail.next = head
    # head 10 20 30 40 50 head
    
    k = k % l
    
    new_head_step = l - k
    
    new_tail = head
    for _ in range(new_head_step-1):
        new_tail = new_tail.next
        
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head
    
        
    
    
def printt(head):
    while head is not None:
        print(head.val,end="=>")
        head = head.next
    

printt(rotateList(head,k))