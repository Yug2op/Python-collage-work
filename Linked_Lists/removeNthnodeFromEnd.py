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


def delFromLast(head,n):
    dummy = Node(0)
    dummy.next = head
    slow = fast = dummy
    for _ in range(n+1):
        fast = fast.next
    while fast is not None:
        fast= fast.next
        slow = slow.next
        
    slow.next = slow.next.next   
    return dummy.next 
n = int(input())

def printt(head):
    while head is not None:
        print(head.val)
        head = head.next

printt(delFromLast(head,n))