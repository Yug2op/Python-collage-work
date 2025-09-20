class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
        
def fsum(root):
    if root is None:
        return 0
    
    x = fsum(root.left)
    y = fsum(root.right)
    
    return x + y + root.val
    
    
root = None # Tree is empty
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.left.right.left = TreeNode(70)
root.right.right = TreeNode(60)


print(fsum(root))