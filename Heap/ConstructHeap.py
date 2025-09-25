# heap is kind of complete binary tree 
# min heao and max heap
# min heap:- parent node is smaller than its child nodes(left subtree and right subtree)
# eg:-
#        10
#      /    \
#     15     30
#    /  \   /  \
#   40  50 100  40
# max heap:- parent node is greater than its child nodes(left subtree and right subtree)
# eg:-
#        100
#      /     \  
#     50      30
#    /  \    /  \
#   20   10  5    1

# heap operations:- push, pop, top, size,empty
# push:- insert an element in the heap
# pop:- delete the root node of the heap
# top:- return the root node of the heap
# size:- return the size of the heap
# empty:- return true if heap is empty otherwise false
# index of parent node = (i-1)//2
# index of left child node = 2*i + 1
# index of right child node = 2*i + 2

import heapq
l = [] # internal representation of heap
heapq.heappush(l,3) # push operation
heapq.heappush(l,2)
heapq.heappush(l,5)
heapq.heappush(l,4)
heapq.heappush(l,1)

print(l) # heappush() creates min heap by default

# min heap
while len(l) > 0:
    print(heapq.heappop(l))
    
# max heap
l = []
heapq.heappush(l,-3) # push operation
heapq.heappush(l,-2)
heapq.heappush(l,-5)    
heapq.heappush(l,-4)
heapq.heappush(l,-1)
print(l) # heappush() creates min heap by default
while len(l) > 0:
    print(-heapq.heappop(l))
# to get max heap we can insert negative of the elements and while popping we can again take negative of the popped element
# time complexity of push and pop operation is O(log n)
# time complexity of top operation is O(1)

# other way to create heap

# using heapify() function
l = [3,2,5,4,1]
heapq.heapify(l)
print(l)
# min heap
while len(l) > 0:
    print(heapq.heappop(l))
    
# max heap
l = [-3,-2,-5,-4,-1]
heapq.heapify(l)
print(l)
while l:
    print(-heapq.heappop(l))