class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
root = None # Tree is empty
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.left.right.left = TreeNode(70)
root.right.right = TreeNode(60)

# Pre-order Traversal   Root -> Left -> Right

def f(root):
    # Base Case
    if root is None:
        print(-1)
        return
    # recursive Case
    
    print(root.val,end=" ")
    f(root.left)
    f(root.right)
    
f(root)
print()

# In-Order Traversal Left -> Root -> Right
def f1(root):
    # Base Case
    if root is None:
        print(-1)
        return
    # recursive Case
    
    f1(root.left)
    print(root.val,end=" ")
    f1(root.right)
    
f1(root)
print()


# Post-Order Traversal Left -> Right -> Root
def f2(root):
    # Base Case
    if root is None:
        print(-1)
        return
    # recursive Case
    
    f2(root.left)
    f2(root.right)
    print(root.val,end=" ")
    
f2(root)


