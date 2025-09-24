from collections import deque
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfsLineWise(root):
    if root is None:
        return 
    queue = deque()
    queue.append(root)
    queue.append(None)  # Marker for end of level
    while queue:
        current = queue.popleft()
        if current is None:
            print()  # End of current level
            if queue:  # If there are more nodes to process
                queue.append(None)  # Add marker for next level
        else:
            print(current.value,end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

root = None
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.right = TreeNode(60)
root.left.right.left = TreeNode(70)

# time: O(n)
# space: O(n)

bfsLineWise(root)

